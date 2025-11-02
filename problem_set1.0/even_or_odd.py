#!/usr/bin/env python3
"""even_or_odd.py

Advanced module for determining if a number is even or odd.

This module demonstrates multiple approaches to check number parity,
including modulo operation, bitwise AND, and bit shifting. It serves
both as a practical utility and an educational tool for understanding
different algorithmic approaches to a simple problem.

Methods Implemented:
    1. Modulo Operation (% 2)
    2. Bitwise AND (& 1)
    3. Bit Shift and Comparison
    4. Division and Integer Comparison

Features:
    - Multiple checking algorithms
    - Input validation and error handling
    - Command-line argument support
    - Batch processing capability
    - Binary representation display
    - Performance comparison

Author: [Your Name]
Date: [Current Date]
Python Version: 3.8+
"""

import argparse
import sys
import time
from typing import Union, Tuple, List, Optional
from enum import Enum
from dataclasses import dataclass


class CheckMethod(Enum):
    """Enumeration of available even/odd checking methods."""
    MODULO = "modulo"
    BITWISE = "bitwise"
    BITSHIFT = "bitshift"
    DIVISION = "division"
    ALL = "all"


@dataclass
class ParityResult:
    """Data class to store parity check results."""
    number: int
    is_even: bool
    method: str
    binary_repr: str
    explanation: str


class ParityChecker:
    """Class to handle various even/odd checking operations."""

    def __init__(self, verbose: bool = False):
        """
        Initialize the ParityChecker.

        Args:
            verbose: If True, provides detailed output
        """
        self.verbose = verbose

    def check_modulo(self, number: int) -> Tuple[bool, str]:
        """
        Check if number is even using modulo operation.

        This is the most common and intuitive method.
        Even numbers have remainder 0 when divided by 2.

        Time Complexity: O(1)

        Args:
            number: Integer to check

        Returns:
            Tuple of (is_even, explanation)
        """
        is_even = number % 2 == 0
        explanation = f"{number} % 2 = {number % 2}, so it's {'even' if is_even else 'odd'}"
        return is_even, explanation

    def check_bitwise(self, number: int) -> Tuple[bool, str]:
        """
        Check if number is even using bitwise AND operation.

        In binary, even numbers have 0 in the least significant bit (LSB),
        odd numbers have 1. AND with 1 extracts the LSB.

        Time Complexity: O(1) - Often faster than modulo

        Args:
            number: Integer to check

        Returns:
            Tuple of (is_even, explanation)
        """
        is_even = (number & 1) == 0
        explanation = (f"{number} & 1 = {number & 1}, "
                      f"LSB is {'0 (even)' if is_even else '1 (odd)'}")
        return is_even, explanation

    def check_bitshift(self, number: int) -> Tuple[bool, str]:
        """
        Check if number is even using bit shifting.

        Right shift by 1 (divide by 2), then left shift by 1 (multiply by 2).
        If the result equals original, the number is even.

        Time Complexity: O(1)

        Args:
            number: Integer to check

        Returns:
            Tuple of (is_even, explanation)
        """
        shifted = (number >> 1) << 1
        is_even = shifted == number
        explanation = (f"({number} >> 1) << 1 = {shifted}, "
                      f"{'equals' if is_even else 'not equal to'} original")
        return is_even, explanation

    def check_division(self, number: int) -> Tuple[bool, str]:
        """
        Check if number is even using division.

        Divide by 2 and check if the result is an integer
        (no fractional part).
        
        Time Complexity: O(1)
        
        Args:
            number: Integer to check
            
        Returns:
            Tuple of (is_even, explanation)
        """
        result = number / 2
        is_even = result == int(result)
        explanation = (f"{number} / 2 = {result}, "
                      f"{'no' if is_even else 'has'} fractional part")
        return is_even, explanation
    
    def get_binary_representation(self, number: int) -> str:
        """
        Get binary representation of a number.
        
        Args:
            number: Integer to convert
            
        Returns:
            Binary string representation
        """
        # Handle negative numbers
        if number < 0:
            # Python uses two's complement for negative numbers
            return f"{bin(number)} (two's complement)"
        return bin(number)
    
    def check_parity(self, number: int, method: CheckMethod) -> ParityResult:
        """
        Check number parity using specified method.
        
        Args:
            number: Integer to check
            method: Method to use for checking
            
        Returns:
            ParityResult with check details
        """
        binary_repr = self.get_binary_representation(number)
        
        # Select appropriate checking method
        if method == CheckMethod.MODULO:
            is_even, explanation = self.check_modulo(number)
        elif method == CheckMethod.BITWISE:
            is_even, explanation = self.check_bitwise(number)
        elif method == CheckMethod.BITSHIFT:
            is_even, explanation = self.check_bitshift(number)
        elif method == CheckMethod.DIVISION:
            is_even, explanation = self.check_division(number)
        else:
            raise ValueError(f"Unknown method: {method}")
        
        return ParityResult(
            number=number,
            is_even=is_even,
            method=method.value,
            binary_repr=binary_repr,
            explanation=explanation
        )
    
    def check_multiple(self, numbers: List[int], method: CheckMethod = CheckMethod.MODULO) -> List[ParityResult]:
        """
        Check parity for multiple numbers.
        
        Args:
            numbers: List of integers to check
            method: Method to use for checking
            
        Returns:
            List of ParityResult objects
        """
        return [self.check_parity(num, method) for num in numbers]
    
    def benchmark_methods(self, number: int, iterations: int = 1000000) -> dict:
        """
        Benchmark different parity checking methods.
        
        Args:
            number: Number to check
            iterations: Number of iterations for benchmarking
            
        Returns:
            Dictionary with timing results for each method
        """
        methods = [
            (CheckMethod.MODULO, self.check_modulo),
            (CheckMethod.BITWISE, self.check_bitwise),
            (CheckMethod.BITSHIFT, self.check_bitshift),
            (CheckMethod.DIVISION, self.check_division)
        ]
        
        results = {}
        for method_enum, method_func in methods:
            start_time = time.perf_counter()
            for _ in range(iterations):
                method_func(number)
            end_time = time.perf_counter()
            results[method_enum.value] = end_time - start_time
        
        return results


def is_even_or_odd(number: int) -> str:
    """
    Determine if a number is even or odd (backward compatible function).
    
    This function maintains compatibility with the original implementation
    while using the new ParityChecker internally.

    Args:
        number: The integer to check

    Returns:
        "Even" if the number is even, "Odd" if the number is odd
        
    Example:
        >>> is_even_or_odd(4)
        'Even'
        >>> is_even_or_odd(5)
        'Odd'
    """
    checker = ParityChecker()
    result = checker.check_parity(number, CheckMethod.MODULO)
    return "Even" if result.is_even else "Odd"


def validate_input(value: str) -> int:
    """
    Validate and convert string input to integer.
    
    Args:
        value: String value to validate
        
    Returns:
        Validated integer
        
    Raises:
        ValueError: If input is not a valid integer
    """
    try:
        return int(value)
    except ValueError:
        raise ValueError(f"'{value}' is not a valid integer")


def display_result(result: ParityResult, detailed: bool = False) -> None:
    """
    Display parity check result.
    
    Args:
        result: ParityResult to display
        detailed: If True, show detailed information
    """
    parity = "EVEN" if result.is_even else "ODD"
    
    print(f"\n{'='*50}")
    print(f"Number: {result.number} is {parity}")
    print(f"{'='*50}")
    
    if detailed:
        print(f"Method: {result.method.upper()}")
        print(f"Binary: {result.binary_repr}")
        print(f"Explanation: {result.explanation}")


def interactive_mode(checker: ParityChecker) -> None:
    """
    Run interactive mode for parity checking.
    
    Args:
        checker: ParityChecker instance
    """
    while True:
        print("\n" + "="*60)
        print("EVEN OR ODD CHECKER - INTERACTIVE MODE")
        print("="*60)
        
        # Get input
        user_input = input("\nEnter an integer (or 'quit' to exit): ").strip()
        
        if user_input.lower() == 'quit':
            print("Goodbye!")
            break
        
        # Validate input
        try:
            number = validate_input(user_input)
        except ValueError as e:
            print(f"❌ Error: {e}")
            continue
        
        # Display menu
        print("\nSelect checking method:")
        print("1. Modulo (% operator)")
        print("2. Bitwise (& operator)")
        print("3. Bit Shift (>> and << operators)")
        print("4. Division (/ operator)")
        print("5. Compare All Methods")
        print("6. Benchmark Performance")
        
        choice = input("\nEnter your choice (1-6): ").strip()
        
        if choice == '1':
            result = checker.check_parity(number, CheckMethod.MODULO)
            display_result(result, detailed=True)
        elif choice == '2':
            result = checker.check_parity(number, CheckMethod.BITWISE)
            display_result(result, detailed=True)
        elif choice == '3':
            result = checker.check_parity(number, CheckMethod.BITSHIFT)
            display_result(result, detailed=True)
        elif choice == '4':
            result = checker.check_parity(number, CheckMethod.DIVISION)
            display_result(result, detailed=True)
        elif choice == '5':
            # Compare all methods
            for method in [CheckMethod.MODULO, CheckMethod.BITWISE, 
                          CheckMethod.BITSHIFT, CheckMethod.DIVISION]:
                result = checker.check_parity(number, method)
                display_result(result, detailed=True)
        elif choice == '6':
            # Benchmark performance
            print("\nBenchmarking methods (1 million iterations)...")
            timings = checker.benchmark_methods(number)
            print("\nPerformance Results:")
            for method, time_taken in sorted(timings.items(), key=lambda x: x[1]):
                print(f"  {method:10s}: {time_taken:.4f} seconds")
        else:
            print("❌ Invalid choice!")
        
        # Continue prompt
        if input("\nCheck another number? (y/n): ").lower() != 'y':
            print("Thank you for using Even or Odd Checker!")
            break


def main() -> None:
    """
    Main function with CLI support and error handling.
    
    Provides both command-line and interactive modes for checking
    if numbers are even or odd using various methods.
    """
    parser = argparse.ArgumentParser(
        description="Check if a number is even or odd using various methods",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s                      # Interactive mode
  %(prog)s 42                   # Check single number
  %(prog)s 1 2 3 4 5           # Check multiple numbers
  %(prog)s 42 -m bitwise       # Use bitwise method
  %(prog)s 42 -m all           # Try all methods
  %(prog)s 42 -d               # Detailed output
  %(prog)s 42 --benchmark      # Benchmark all methods
        """
    )
    
    parser.add_argument(
        'numbers',
        nargs='*',
        help='Number(s) to check'
    )
    parser.add_argument(
        '-m', '--method',
        choices=['modulo', 'bitwise', 'bitshift', 'division', 'all'],
        default='modulo',
        help='Method to use for checking (default: modulo)'
    )
    parser.add_argument(
        '-d', '--detailed',
        action='store_true',
        help='Show detailed output'
    )
    parser.add_argument(
        '--benchmark',
        action='store_true',
        help='Benchmark all methods'
    )
    
    args = parser.parse_args()
    
    # Create checker instance
    checker = ParityChecker(verbose=args.detailed)
    
    # Handle different modes
    if args.numbers:
        # Command-line mode
        try:
            numbers = [validate_input(n) for n in args.numbers]
        except ValueError as e:
            print(f"❌ Error: {e}")
            sys.exit(1)
        
        # Map method string to enum
        method_map = {
            'modulo': CheckMethod.MODULO,
            'bitwise': CheckMethod.BITWISE,
            'bitshift': CheckMethod.BITSHIFT,
            'division': CheckMethod.DIVISION,
            'all': CheckMethod.ALL
        }
        
        selected_method = method_map[args.method]
        
        # Process each number
        for number in numbers:
            if args.benchmark:
                print(f"\nBenchmarking for number {number}...")
                timings = checker.benchmark_methods(number)
                for method, time_taken in sorted(timings.items(), key=lambda x: x[1]):
                    print(f"  {method:10s}: {time_taken:.4f} seconds")
            elif selected_method == CheckMethod.ALL:
                for method in [CheckMethod.MODULO, CheckMethod.BITWISE,
                             CheckMethod.BITSHIFT, CheckMethod.DIVISION]:
                    result = checker.check_parity(number, method)
                    display_result(result, detailed=args.detailed)
            else:
                result = checker.check_parity(number, selected_method)
                display_result(result, detailed=args.detailed)
    else:
        # Interactive mode
        interactive_mode(checker)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nOperation cancelled by user.")
        sys.exit(0)
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        sys.exit(1)
