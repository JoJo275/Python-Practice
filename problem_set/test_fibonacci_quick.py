"""Quick test for fibonacci function."""
from fibonacci import fibonacci

print("=== Testing fibonacci function ===\n")

# Test valid inputs
test_cases = [(0, 0), (1, 1), (5, 5), (10, 55), (15, 610), (20, 6765)]

print("Valid input tests:")
for n, expected in test_cases:
    result = fibonacci(n)
    status = "✓" if result == expected else "✗"
    print(f"{status} fibonacci({n}) = {result} (expected {expected})")

# Test error handling
print("\nError handling test:")
try:
    fibonacci(-5)
    print("✗ Failed: Should have raised ValueError for negative input")
except ValueError as e:
    print(f"✓ Success: Raised ValueError - {e}")

print("\n=== All tests completed ===")
