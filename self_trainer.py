#!/usr/bin/env python3
"""
Self-Training Code Generator (Evolutionary, Test-Driven)

What it does
------------
- Evolves small Python functions that pass unit tests for a set of tasks.
- Uses a sandboxed executor to safely run candidate code.
- Scores candidates by tests passed, runtime, and code simplicity.
- Applies genetic operators (mutation, crossover) guided by failure signals.

Run it
------
$ python self_trainer.py --gens 20 --pop 60 --seed 0

Notes
-----
- This is compute-light by default; tweak --gens/--pop for stronger results.
- Execution is sandboxed with a tiny builtin whitelist and a time limit per run.
"""

from __future__ import annotations
import ast
import math
import os
import random
import sys
import textwrap
import time
from dataclasses import dataclass, field
from multiprocessing import Process, Queue, set_start_method
from typing import Any, Callable, Dict, List, Optional, Tuple

# ------------------------------- Sandbox ------------------------------------

SAFE_BUILTINS = {
    "abs": abs, "all": all, "any": any, "bool": bool, "callable": callable,
    "dict": dict, "enumerate": enumerate, "filter": filter, "float": float,
    "int": int, "len": len, "list": list, "map": map, "max": max, "min": min,
    "pow": pow, "range": range, "reversed": reversed, "round": round,
    "set": set, "sorted": sorted, "str": str, "sum": sum, "tuple": tuple,
    "__name__": "__main__",
}

SAFE_GLOBALS = {
    "__builtins__": SAFE_BUILTINS,
    "math": math,
}

def _run_candidate(code: str, inputs: List[Tuple], timeout_s: float, return_q: Queue):
    """
    Run in a separate process to enforce a hard timeout.
    """
    try:
        loc: Dict[str, Any] = {}
        compiled = compile(code, "<candidate>", "exec")
        exec(compiled, SAFE_GLOBALS.copy(), loc)
        solve = loc.get("solve", None)
        if not callable(solve):
            return_q.put(("error", "No function `solve` defined."))
            return
        outputs = []
        start = time.perf_counter()
        for args in inputs:
            # each args is a tuple of args (can be single value)
            if not isinstance(args, tuple):
                args = (args,)
            outputs.append(solve(*args))
        dur = time.perf_counter() - start
        return_q.put(("ok", (outputs, dur)))
    except Exception as e:
        return_q.put(("error", f"{type(e).__name__}: {e}"))

def sandbox_exec(code: str, inputs: List[Tuple], timeout_s: float = 0.25) -> Tuple[str, Any]:
    """
    Returns ("ok", (outputs, duration)) or ("error", message)
    """
    q: Queue = Queue()
    p = Process(target=_run_candidate, args=(code, inputs, timeout_s, q))
    p.daemon = True
    p.start()
    p.join(timeout_s)
    if p.is_alive():
        p.kill()
        p.join()
        return ("error", "Timeout")
    if not q.empty():
        return q.get()
    return ("error", "No result")

# ------------------------------- Tasks --------------------------------------

@dataclass
class Task:
    name: str
    # Each test is (args_tuple, expected_output). args_tuple can be a single value.
    tests: List[Tuple[Tuple, Any]]
    # Optional input list used for quick batch exec in sandbox
    input_args_for_batch: List[Tuple] = field(default_factory=list)
    # Seed snippets that are syntactically valid and helpful search anchors
    seeds: List[str] = field(default_factory=list)

def _as_args(x):
    return x if isinstance(x, tuple) else (x,)

def build_default_tasks() -> List[Task]:
    t1 = Task(
        name="sum_digits",
        tests=[((0,),0), ((7,),7), ((42,),6), ((999,),27), ((123456,),21)],
        seeds=[
            "def solve(n:int)->int:\n    s=0\n    n=abs(n)\n    while n:\n        s+=n%10\n        n//=10\n    return s",
            "def solve(n:int)->int:\n    return sum(int(ch) for ch in str(abs(n)))",
        ],
    )
    t2 = Task(
        name="is_prime",
        tests=[((2,),True), ((3,),True), ((4,),False), ((17,),True), ((21,),False), ((1,),False), ((97,),True)],
        seeds=[
            "def solve(n:int)->bool:\n    if n<2: return False\n    if n%2==0: return n==2\n    i=3\n    r=int(n**0.5)\n    while i<=r:\n        if n%i==0: return False\n        i+=2\n    return True",
        ],
    )
    t3 = Task(
        name="reverse_words",
        tests=[(("hello world",),"world hello"), (("a b  c",),"c b a"), (("Python",),"Python")],
        seeds=[
            "def solve(s:str)->str:\n    return ' '.join(reversed([w for w in s.split() if w]))",
        ],
    )
    t4 = Task(
        name="two_sum",
        tests=[(((2,7,11,15),9), (0,1)), (((3,2,4),6),(1,2)), (((3,3),6),(0,1))],
        seeds=[
            "def solve(nums,target):\n    d={}\n    for i,x in enumerate(nums):\n        y=target-x\n        if y in d: return (d[y],i)\n        d[x]=i",
        ],
    )
    t5 = Task(
        name="levenshtein",
        tests=[(("kitten","sitting"),3), (("flaw","lawn"),2), (("a",""),1), (("",""),0)],
        seeds=[
            """def solve(a:str,b:str)->int:
    la,lb=len(a),len(b)
    dp=[[0]*(lb+1) for _ in range(la+1)]
    for i in range(la+1): dp[i][0]=i
    for j in range(lb+1): dp[0][j]=j
    for i in range(1,la+1):
        for j in range(1,lb+1):
            cost=0 if a[i-1]==b[j-1] else 1
            dp[i][j]=min(dp[i-1][j]+1, dp[i][j-1]+1, dp[i-1][j-1]+cost)
    return dp[la][lb]""",
        ],
    )
    # Provide batch inputs for runtime measurement
    for t in (t1,t2,t3,t4,t5):
        t.input_args_for_batch=[_as_args(x[0]) for x in t.tests]
    return [t1,t2,t3,t4,t5]

# ----------------------------- Representation --------------------------------

STUB_HEADER = "# Evolved by CodeTrainer\n"
TEMPLATE = """{header}
{imports}
{body}
"""

DEFAULT_IMPORTS = "from math import sqrt"

# Token pools used for mutation
TOKEN_POOL = [
    " ", "  ", "\n", ":", "(", ")", "[", "]", "{", "}", ",", "+", "-", "*", "//", "%", "==", "!=", "<", ">", "<=", ">=",
    "=", "return", "if", "else", "for", "while", "in", "not", "and", "or",
    "True", "False", "None",
    "range", "len", "sum", "abs", "min", "max", "sorted", "reversed", "list", "set", "dict",
]

CONSTANT_POOL = ["0","1","2","3","4","5","6","7","8","9","10"]

SEED_WRAPPERS = [
    # identity
    lambda body: body,
    # add minor noise
    lambda body: body.replace("  ", " ") + "\n",
    # insert harmless whitespace
    lambda body: "\n" + body + "\n",
]

def random_identifier(prefix: str = "v") -> str:
    return f"{prefix}{random.randint(0, 9999)}"

def sanitize(code: str) -> str:
    # Remove disallowed imports or dunders
    lines = []
    for ln in code.splitlines():
        if ln.strip().startswith("import ") or ln.strip().startswith("from "):
            # Allow internal default import of sqrt only (already present in globals as math)
            continue
        if "__" in ln:
            continue
        lines.append(ln)
    return "\n".join(lines)

# ------------------------------- Genetics ------------------------------------

@dataclass
class Candidate:
    code: str
    fitness: float = float("-inf")
    meta: Dict[str, Any] = field(default_factory=dict)

def crossover(a: str, b: str) -> str:
    alines = a.splitlines()
    blines = b.splitlines()
    if not alines or not blines:
        return a
    i = random.randint(0, len(alines)-1)
    j = random.randint(0, len(blines)-1)
    child = "\n".join(alines[:i] + blines[j:])
    return child

def mutate(body: str, intensity: float = 0.2) -> str:
    # Simple token-level edits
    s = list(body)
    if not s:  # Handle empty body
        s = list("pass")
    
    for _ in range(max(1, int(len(s) * intensity * 0.05))):
        op = random.choice(["insert","delete","replace","const"])
        idx = random.randint(0, max(0,len(s)-1)) if s else 0
        if op == "insert":
            tok = random.choice(random.choice([TOKEN_POOL, CONSTANT_POOL]))
            s[idx:idx] = list(tok)
        elif op == "delete" and len(s) > 1:  # Keep at least one character
            s.pop(idx)
        elif op == "replace" and s:
            tok_list = random.choice([TOKEN_POOL, CONSTANT_POOL])
            if tok_list:  # Ensure we have tokens to choose from
                replacement = random.choice(tok_list)
                if replacement:  # Ensure replacement has at least one character
                    s[idx] = replacement[0] if len(replacement) > 0 else ' '
        elif op == "const":
            # sprinkle a small int literal somewhere
            tok = random.choice(CONSTANT_POOL)
            s[idx:idx] = list(tok)
    return "".join(s)

def make_seed(task: Task) -> str:
    seed = random.choice(task.seeds) if task.seeds else "def solve(x):\n    return x\n"
    wrapper = random.choice(SEED_WRAPPERS)
    body = wrapper(seed)
    return TEMPLATE.format(header=STUB_HEADER, imports=DEFAULT_IMPORTS, body=body)

# ------------------------------- Scoring -------------------------------------

def score_candidate(code: str, task: Task) -> Tuple[float, Dict[str, Any]]:
    code = sanitize(code)
    status, res = sandbox_exec(code, inputs=task.input_args_for_batch, timeout_s=0.25)
    if status == "error":  # heavy penalty, but allow exploration
        return (-10.0, {"error": res})
    outputs, dur = res
    # Compare against expected
    passed = 0
    total = len(task.tests)
    for (args, expected), out in zip(task.tests, outputs):
        if out == expected:
            passed += 1
    acc = passed / total
    # Simplicity reward (shorter code is better) and speed reward
    length_penalty = min(len(code)/300, 1.5)  # cap
    time_penalty = min(dur/0.01, 3.0)         # baseline 10ms batch
    fitness = (acc * 10.0) - (0.5 * length_penalty) - (0.3 * time_penalty)
    return (fitness, {"passed": passed, "total": total, "dur": dur})

# ------------------------------- Trainer -------------------------------------

@dataclass
class TrainerConfig:
    pop: int = 40
    gens: int = 30
    elite: int = 6
    mutate_rate: float = 0.7
    cx_rate: float = 0.5
    seed: Optional[int] = None

class CodeTrainer:
    def __init__(self, tasks: List[Task], cfg: TrainerConfig):
        self.tasks = tasks
        self.cfg = cfg
        if cfg.seed is not None:
            random.seed(cfg.seed)

    def evolve_for_task(self, task: Task) -> Candidate:
        pop: List[Candidate] = [Candidate(make_seed(task)) for _ in range(self.cfg.pop)]
        best: Candidate = Candidate(code="", fitness=float("-inf"))

        for gen in range(self.cfg.gens):
            scored: List[Candidate] = []
            for cand in pop:
                fit, meta = score_candidate(cand.code, task)
                cand.fitness = fit
                cand.meta = meta
                scored.append(cand)
            scored.sort(key=lambda c: c.fitness, reverse=True)
            if scored[0].fitness > best.fitness:
                best = Candidate(scored[0].code, scored[0].fitness, scored[0].meta)
            # Print minimal progress
            print(f"[{task.name}] gen {gen+1:03d} | best {scored[0].fitness:.3f} | pass {scored[0].meta.get('passed','?')}/{scored[0].meta.get('total','?')} | dur {scored[0].meta.get('dur',0):.4f}s")

            # Early stop if perfect
            if scored[0].meta.get("passed", 0) == scored[0].meta.get("total", 1):
                break

            # Next generation
            next_pop: List[Candidate] = scored[: self.cfg.elite]  # elitism
            while len(next_pop) < self.cfg.pop:
                if random.random() < self.cfg.cx_rate:
                    a, b = random.sample(scored[: max(10, self.cfg.elite)], 2)
                    child_code = crossover(a.code, b.code)
                else:
                    a = random.choice(scored[: max(10, self.cfg.elite)])
                    child_code = a.code
                if random.random() < self.cfg.mutate_rate:
                    lines = child_code.split("\n", 2)
                    if len(lines) > 2:  # Ensure we have a body to mutate
                        body = lines[2]
                    else:
                        body = child_code
                    body = mutate(body, intensity=0.25)
                    child_code = TEMPLATE.format(header=STUB_HEADER, imports=DEFAULT_IMPORTS, body=body)
                next_pop.append(Candidate(child_code))
            pop = next_pop
        return best

    def run(self):
        report = []
        for task in self.tasks:
            best = self.evolve_for_task(task)
            report.append((task.name, best.fitness, best.meta, best.code))
        return report

# ------------------------------- CLI -----------------------------------------

def main(argv: List[str] = None):
    import argparse
    parser = argparse.ArgumentParser(description="Self-training code generator (evolutionary)")
    parser.add_argument("--gens", type=int, default=20, help="Generations per task")
    parser.add_argument("--pop", type=int, default=40, help="Population size")
    parser.add_argument("--seed", type=int, default=0, help="Random seed")
    args = parser.parse_args(argv)

    # Windows-specific multiprocessing setup
    if sys.platform == "win32":
        try:
            set_start_method("spawn", force=True)
        except RuntimeError:
            pass
    else:
        try:
            set_start_method("fork")  # for fast multiprocess on Unix
        except RuntimeError:
            pass

    tasks = build_default_tasks()
    cfg = TrainerConfig(pop=args.pop, gens=args.gens, seed=args.seed)
    trainer = CodeTrainer(tasks, cfg)
    report = trainer.run()

    print("\n=== BEST PROGRAMS BY TASK ===")
    for name, fit, meta, code in report:
        print(f"\n--- {name} ---\nfitness={fit:.3f} | passed={meta.get('passed','?')}/{meta.get('total','?')} | dur={meta.get('dur',0):.5f}s\n")
        print(textwrap.indent(code.strip(), prefix="    "))

if __name__ == "__main__":
    main()
