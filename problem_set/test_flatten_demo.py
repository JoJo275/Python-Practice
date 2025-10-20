"""Demo and test script for flatten.py functionality."""
from flatten import flatten, _get_depth, parse_list_input

print("=" * 60)
print("=== Flatten Function Test Suite ===")
print("=" * 60)

# Test 1: Basic flattening
print("\n1. Basic Flattening Tests:")
test_cases = [
    ([1, 2, 3], [1, 2, 3], "Flat list (no nesting)"),
    ([1, [2, 3]], [1, 2, 3], "Simple nesting"),
    ([[1, 2], [3, 4]], [1, 2, 3, 4], "Multiple nested groups"),
    ([1, [2, [3, 4], 5], 6], [1, 2, 3, 4, 5, 6], "Mixed nesting"),
    ([[[1]]], [1], "Deep single element"),
    ([], [], "Empty list"),
]

for input_list, expected, description in test_cases:
    result = flatten(input_list)
    status = "✓" if result == expected else "✗"
    print(f"{status} {description}")
    print(f"  Input:    {input_list}")
    print(f"  Output:   {result}")
    print(f"  Expected: {expected}")

# Test 2: Depth calculation
print("\n2. Depth Calculation Tests:")
depth_tests = [
    ([1, 2, 3], 1, "Flat list"),
    ([1, [2, 3]], 2, "One level deep"),
    ([1, [2, [3, 4]]], 3, "Two levels deep"),
    ([1, [2, [3, [4, [5]]]]], 5, "Four levels deep"),
    ([], 1, "Empty list"),
]

for lst, expected_depth, description in depth_tests:
    result = _get_depth(lst)
    status = "✓" if result == expected_depth else "✗"
    print(f"{status} {description}: {result} levels", end="")
    print(f" (expected {expected_depth})")

# Test 3: Input parsing tests
print("\n3. Input Parsing Tests:")
parse_tests = [
    ("[1, 2, 3]", True, "Simple flat list"),
    ("[1, [2, 3]]", True, "Nested list"),
    ("[[1], [2], [3]]", True, "Multiple nested elements"),
    ("[1, 'hello', 3.14]", True, "Mixed types"),
    ("", False, "Empty string"),
    ("not a list", False, "Invalid format"),
    ("123", False, "Number instead of list"),
    ("[1, 2,", False, "Incomplete list"),
]

for input_str, should_succeed, description in parse_tests:
    try:
        result = parse_list_input(input_str)
        if should_succeed:
            print(f"✓ {description}: Parsed successfully → {result}")
        else:
            print(f"✗ {description}: Should have failed but got {result}")
    except (ValueError, SyntaxError) as e:
        if not should_succeed:
            print(f"✓ {description}: Correctly rejected")
        else:
            print(f"✗ {description}: Should have succeeded but got error: {e}")

# Test 4: Complex nested structures
print("\n4. Complex Structure Tests:")
complex_tests = [
    [1, [2, [3, [4, [5, [6]]]]], 7],
    [[[[[[1]]]]]],
    [[], [1], [[2]], [[[3]]]],
    [1, [], 2, [[]], 3, [[[]]]],
]

for complex_list in complex_tests:
    result = flatten(complex_list)
    depth = _get_depth(complex_list)
    print(f"Input depth {depth}: {complex_list}")
    print(f"  → Flattened: {result}")

print("\n" + "=" * 60)
print("=== All Tests Completed ===")
print("=" * 60)
print("\nTo run the interactive version:")
print("  python flatten.py")
print("=" * 60)
