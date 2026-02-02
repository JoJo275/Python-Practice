# !/usr/bin/env python3
"""e6.py
A demonstration of Python's random module.
"""

import random

# Set seed for reproducibility (optional - comment out for true randomness)
# random.seed(42)

# ============================================
# 1. Random integers
# ============================================
print("=== Random Integers ===")
print(f"randint(1, 10): {random.randint(1, 10)}")  # Inclusive on both ends
print(f"randrange(1, 10): {random.randrange(1, 10)}")  # Exclusive on upper end
print(f"randrange(0, 100, 5): {random.randrange(0, 100, 5)}")  # With step

# ============================================
# 2. Random floats
# ============================================
print("\n=== Random Floats ===")
print(f"random(): {random.random()}")  # 0.0 to 1.0
print(f"uniform(1.5, 6.5): {random.uniform(1.5, 6.5)}")  # Range with floats

# ============================================
# 3. Sequences - choice, choices, sample
# ============================================
print("\n=== Working with Sequences ===")
colors = ["red", "green", "blue", "yellow", "purple"]
print(f"Original list: {colors}")
print(f"choice(colors): {random.choice(colors)}")  # Single random element
print(f"choices(colors, k=3): {random.choices(colors, k=3)}")  # With replacement
print(f"sample(colors, k=3): {random.sample(colors, k=3)}")  # Without replacement

# Weighted choices
print("\n=== Weighted Choices ===")
outcomes = ["win", "lose", "draw"]
weights = [0.2, 0.5, 0.3]  # 20% win, 50% lose, 30% draw
results = random.choices(outcomes, weights=weights, k=10)
print(f"10 weighted outcomes: {results}")

# ============================================
# 4. Shuffle a list (in-place)
# ============================================
print("\n=== Shuffling ===")
deck = list(range(1, 11))
print(f"Original deck: {deck}")
random.shuffle(deck)
print(f"Shuffled deck: {deck}")

# ============================================
# 5. Practical example: Dice roller
# ============================================
print("\n=== Dice Roller ===")
def roll_dice(num_dice: int = 2, sides: int = 6) -> list[int]:
    """Roll multiple dice and return results."""
    return [random.randint(1, sides) for _ in range(num_dice)]

rolls = roll_dice(3, 6)
print(f"Rolling 3 six-sided dice: {rolls} (Total: {sum(rolls)})")

# ============================================
# 6. Practical example: Password generator
# ============================================
print("\n=== Password Generator ===")
import string

def generate_password(length: int = 12) -> str:
    """Generate a random password."""
    chars = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choices(chars, k=length))

print(f"Generated password: {generate_password(16)}")

# ============================================
# 7. Practical example: Random quote picker
# ============================================
print("\n=== Random Quote ===")
quotes = [
    "The only way to do great work is to love what you do. - Steve Jobs",
    "Code is like humor. When you have to explain it, it's bad. - Cory House",
    "First, solve the problem. Then, write the code. - John Johnson",
    "Simplicity is the soul of efficiency. - Austin Freeman",
]
print(f"Quote of the day: {random.choice(quotes)}")
