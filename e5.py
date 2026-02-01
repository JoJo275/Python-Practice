# !/usr/bin/env python3
"""e5.py

Random module practice

"""

import random

# 1. Generate a random float between 0 and 1
random_float = random.random()
print(f"Random float (0-1): {random_float}")

# 2. Generate a random integer within a range
random_int = random.randint(1, 100)
print(f"Random integer (1-100): {random_int}")

# 3. Choose a random element from a list
colors = ["red", "blue", "green", "yellow", "purple"]
random_color = random.choice(colors)
print(f"Random color: {random_color}")

# 4. Choose multiple random elements (with replacement)
random_colors = random.choices(colors, k=3)
print(f"Random colors (with replacement): {random_colors}")

# 5. Choose multiple random elements (without replacement)
random_sample = random.sample(colors, k=3)
print(f"Random sample (no replacement): {random_sample}")

# 6. Shuffle a list in place
numbers = [1, 2, 3, 4, 5]
random.shuffle(numbers)
print(f"Shuffled numbers: {numbers}")

# 7. Generate a random float within a range
random_uniform = random.uniform(10.5, 20.5)
print(f"Random uniform (10.5-20.5): {random_uniform}")

# 8. Generate random number from normal distribution
random_normal = random.gauss(mu=0, sigma=1)
print(f"Random normal (mean=0, std=1): {random_normal}")

# 9. Set seed for reproducibility
random.seed(42)
reproducible = [random.randint(1, 10) for _ in range(5)]
print(f"Reproducible sequence (seed=42): {reproducible}")

# 10. Practical example: Simulate a dice roll
def roll_dice(num_dice=1):
    """Roll specified number of dice and return results."""
    return [random.randint(1, 6) for _ in range(num_dice)]

dice_results = roll_dice(2)
print(f"Dice roll (2 dice): {dice_results}, Total: {sum(dice_results)}")

# 11. Practical example: Generate a random password
def generate_password(length=12):
    """Generate a random password with letters, digits, and symbols."""
    import string
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

password = generate_password(16)
print(f"Random password: {password}")

# 12. Practical example: Weighted random selection
items = ["common", "uncommon", "rare", "legendary"]
weights = [70, 20, 8, 2]
loot_drop = random.choices(items, weights=weights, k=5)
print(f"Loot drops (weighted): {loot_drop}")
