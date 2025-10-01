"""Solutions for the problem set."""
from collections import deque, defaultdict


def sum_of_even(n):
    """Return the sum of all even numbers from 1 to n inclusive."""
    if n < 1:
        return 0
    # largest even <= n
    m = n if n % 2 == 0 else n - 1
    count = m // 2
    # sum of first k even numbers = k*(k+1)
    return count * (count + 1)


def is_anagram(s1, s2):
    """Return True if s1 and s2 are anagrams.

    Comparison is case-insensitive and ignores spaces and punctuation.
    """
    def normalize(s):
        s = s.lower()
        return ''.join(ch for ch in s if ch.isalnum())

    a = normalize(s1)
    b = normalize(s2)
    return sorted(a) == sorted(b)


def fibonacci(n):
    """Return the nth Fibonacci number.

    fibonacci(0) == 0 and fibonacci(1) == 1. Raises ValueError for n < 0.
    """
    if n < 0:
        raise ValueError("n must be >= 0")
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def flatten(lst):
    """Flatten nested lists of arbitrary depth."""
    out = []

    def _flatten(x):
        if isinstance(x, list):
            for v in x:
                _flatten(v)
        else:
            out.append(x)

    _flatten(lst)
    return out


def group_by_key(items, key):
    """Group list of dicts by value of key; missing key grouped under None."""
    res = defaultdict(list)
    for item in items:
        val = item.get(key, None)
        res[val].append(item)
    return dict(res)


def shortest_path(grid):
    """Return length of shortest path from top-left to bottom-right.

    Grid is a binary 2D list where 0 is open and 1 is a wall. Returns -1
    if no path exists.
    """
    if not grid or not grid[0]:
        return -1
    m, n = len(grid), len(grid[0])
    if grid[0][0] == 1 or grid[m - 1][n - 1] == 1:
        return -1
    if m == 1 and n == 1:
        return 0

    q = deque()
    q.append((0, 0, 0))  # row, col, dist
    visited = [[False] * n for _ in range(m)]
    visited[0][0] = True
    dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    while q:
        r, c, d = q.popleft()
        for dr, dc in dirs:
            nr, nc = r + dr, c + dc
            if (
                0 <= nr < m
                and 0 <= nc < n
                and not visited[nr][nc]
                and grid[nr][nc] == 0
            ):
                if nr == m - 1 and nc == n - 1:
                    return d + 1
                visited[nr][nc] = True
                q.append((nr, nc, d + 1))

    return -1
