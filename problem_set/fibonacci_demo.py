"""Demo script showing fibonacci.py usage."""
from fibonacci import fibonacci

print("=== Fibonacci Calculator Demo ===\n")
print("This demonstrates the interactive fibonacci calculator.")
print("The program handles various types of input and errors:\n")

# Show some example calculations

examples = [
    ("Valid input: 0", 0),
    ("Valid input: 10", 10),
    ("Valid input: 20", 20),
]

for description, n in examples:
    result = fibonacci(n)
    print(f"• {description}: fibonacci({n}) = {result}")

print("\n• Error handling: Negative input (-5)")
try:
    fibonacci(-5)
except ValueError as e:
    print(f"  Correctly raises ValueError: {e}")

print("\n• Invalid input: The program handles non-numeric input gracefully")
print("• Exit options: User can type 'q', 'quit', or 'exit' to quit")
print("• Keyboard interrupt: Ctrl+C is handled gracefully\n")

print("=" * 50)
print("To run the interactive program, use:")
print("  python fibonacci.py")
print("=" * 50)
