#!/usr/bin/env python3
"""swap_variables.py

Advanced module for demonstrating multiple variable swapping techniques in Python.

This module showcases various methods to swap variables in Python, including:
- Tuple unpacking (Pythonic way)
- Arithmetic operations (for numeric values)
- XOR bitwise operation (for integers)
- Traditional temporary variable method

Features:
- Type detection and conversion
- Error handling
- Multiple swap methods demonstration
- Command-line argument support
- Logging capability
- Interactive menu system

Author: [Your Name]
Date: [Current Date]
Python Version: 3.8+
"""

import argparse
import logging
import sys
from enum import Enum
from typing import Any, Tuple, Optional, Union
from dataclasses import dataclass


# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class SwapMethod(Enum):
    """Enumeration of available swap methods."""
    TUPLE_UNPACKING = "tuple"
    ARITHMETIC = "arithmetic"
    XOR = "xor"
    TEMPORARY = "temp"
    ALL = "all"


@dataclass
class SwapResult:
    """Data class to store swap operation results."""
    original_a: Any
    original_b: Any
    swapped_a: Any
    swapped_b: Any
    method: str
    success: bool
    error_message: Optional[str] = None


class VariableSwapper:
    """Class to handle various variable swapping operations."""

    def __init__(self, verbose: bool = False):
        """
        Initialize the VariableSwapper.

        Args:
            verbose: If True, enables detailed logging
        """
        self.verbose = verbose
        if verbose:
            logger.setLevel(logging.DEBUG)

    def detect_type(self, value: str) -> Tuple[Any, type]:
        """
        Detect and convert string input to appropriate type.

        Args:
            value: String value to analyze

        Returns:
            Tuple of (converted_value, detected_type)
        """
        # Try integer conversion
        try:
            return int(value), int
        except ValueError:
            pass

        # Try float conversion
        try:
            return float(value), float
        except ValueError:
            pass

        # Try boolean conversion
        if value.lower() in ('true', 'false'):
            return value.lower() == 'true', bool

        # Default to string
        return value, str

    def swap_tuple_unpacking(self, a: Any, b: Any) -> Tuple[Any, Any]:
        """
        Swap using Python's tuple unpacking method.
        
        Args:
            a: First value
            b: Second value
            
        Returns:
            Tuple of swapped values (b, a)
        """
        logger.debug(f"Swapping {a} and {b} using tuple unpacking")
        return b, a
    
    def swap_arithmetic(self, a: Union[int, float], b: Union[int, float]) -> Tuple[Union[int, float], Union[int, float]]:
        """
        Swap using arithmetic operations (works only with numbers).
        
        Args:
            a: First numeric value
            b: Second numeric value
            
        Returns:
            Tuple of swapped values
            
        Raises:
            TypeError: If values are not numeric
        """
        if not all(isinstance(x, (int, float)) for x in [a, b]):
            raise TypeError("Arithmetic swap requires numeric values")
        
        logger.debug(f"Swapping {a} and {b} using arithmetic method")
        a = a + b
        b = a - b
        a = a - b
        return a, b
    
    def swap_xor(self, a: int, b: int) -> Tuple[int, int]:
        """
        Swap using XOR bitwise operation (works only with integers).
        
        Args:
            a: First integer value
            b: Second integer value
            
        Returns:
            Tuple of swapped values
            
        Raises:
            TypeError: If values are not integers
        """
        if not all(isinstance(x, int) for x in [a, b]):
            raise TypeError("XOR swap requires integer values")
        
        logger.debug(f"Swapping {a} and {b} using XOR method")
        a = a ^ b
        b = a ^ b
        a = a ^ b
        return a, b
    
    def swap_temporary(self, a: Any, b: Any) -> Tuple[Any, Any]:
        """
        Swap using traditional temporary variable method.
        
        Args:
            a: First value
            b: Second value
            
        Returns:
            Tuple of swapped values
        """
        logger.debug(f"Swapping {a} and {b} using temporary variable")
        temp = a
        a = b
        b = temp
        return a, b
    
    def perform_swap(self, a: Any, b: Any, method: SwapMethod) -> SwapResult:
        """
        Perform swap operation using specified method.
        
        Args:
            a: First value
            b: Second value
            method: Swap method to use
            
        Returns:
            SwapResult object containing operation details
        """
        original_a, original_b = a, b
        
        try:
            if method == SwapMethod.TUPLE_UNPACKING:
                a, b = self.swap_tuple_unpacking(a, b)
                
            elif method == SwapMethod.ARITHMETIC:
                a, b = self.swap_arithmetic(a, b)
                
            elif method == SwapMethod.XOR:
                a, b = self.swap_xor(a, b)
                
            elif method == SwapMethod.TEMPORARY:
                a, b = self.swap_temporary(a, b)
                
            return SwapResult(
                original_a=original_a,
                original_b=original_b,
                swapped_a=a,
                swapped_b=b,
                method=method.value,
                success=True
            )
            
        except (TypeError, ValueError) as e:
            logger.error(f"Swap failed: {e}")
            return SwapResult(
                original_a=original_a,
                original_b=original_b,
                swapped_a=original_a,
                swapped_b=original_b,
                method=method.value,
                success=False,
                error_message=str(e)
            )


def display_result(result: SwapResult) -> None:
    """
    Display swap operation result.
    
    Args:
        result: SwapResult object to display
    """
    print(f"\n{'='*50}")
    print(f"Method: {result.method.upper()}")
    print(f"{'='*50}")
    
    if result.success:
        print(f"Before swapping: a = {result.original_a}, b = {result.original_b}")
        print(f"After swapping:  a = {result.swapped_a}, b = {result.swapped_b}")
    else:
        print(f"❌ Swap failed: {result.error_message}")


def interactive_mode(swapper: VariableSwapper) -> None:
    """
    Run interactive mode with menu system.
    
    Args:
        swapper: VariableSwapper instance to use
    """
    while True:
        print("\n" + "="*60)
        print("VARIABLE SWAPPER - INTERACTIVE MODE")
        print("="*60)
        
        # Get input values
        a_str = input("\nEnter the value of variable a (or 'quit' to exit): ").strip()
        if a_str.lower() == 'quit':
            print("Goodbye!")
            break
            
        b_str = input("Enter the value of variable b: ").strip()
        
        # Detect and convert types
        a, a_type = swapper.detect_type(a_str)
        b, b_type = swapper.detect_type(b_str)
        
        print(f"\nDetected types: a={a_type.__name__}, b={b_type.__name__}")
        
        # Display menu
        print("\nSelect swap method:")
        print("1. Tuple Unpacking (works with all types)")
        print("2. Arithmetic (numbers only)")
        print("3. XOR Bitwise (integers only)")
        print("4. Temporary Variable (works with all types)")
        print("5. Demonstrate All Methods")
        
        choice = input("\nEnter your choice (1-5): ").strip()
        
        # Map choice to method
        method_map = {
            '1': SwapMethod.TUPLE_UNPACKING,
            '2': SwapMethod.ARITHMETIC,
            '3': SwapMethod.XOR,
            '4': SwapMethod.TEMPORARY,
            '5': SwapMethod.ALL
        }
        
        if choice not in method_map:
            print("❌ Invalid choice!")
            continue
        
        selected_method = method_map[choice]
        
        # Perform swap(s)
        if selected_method == SwapMethod.ALL:
            methods = [SwapMethod.TUPLE_UNPACKING, SwapMethod.ARITHMETIC, 
                      SwapMethod.XOR, SwapMethod.TEMPORARY]
            for method in methods:
                result = swapper.perform_swap(a, b, method)
                display_result(result)
        else:
            result = swapper.perform_swap(a, b, selected_method)
            display_result(result)
        
        # Ask to continue
        if input("\nDo you want to swap more variables? (y/n): ").lower() != 'y':
            print("Thank you for using Variable Swapper!")
            break


def main() -> None:
    """
    Main function with command-line argument support and enhanced functionality.
    
    This function provides both command-line and interactive modes for
    demonstrating various variable swapping techniques.
    """
    parser = argparse.ArgumentParser(
        description="Demonstrate various variable swapping methods in Python",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s                           # Interactive mode
  %(prog)s -a 10 -b 20              # Swap 10 and 20
  %(prog)s -a hello -b world        # Swap strings
  %(prog)s -a 10 -b 20 -m xor       # Use XOR method
  %(prog)s -a 10 -b 20 -m all       # Try all methods
  %(prog)s -a 10 -b 20 -v           # Verbose output
        """
    )
    
    parser.add_argument('-a', '--first', type=str, help='First value to swap')
    parser.add_argument('-b', '--second', type=str, help='Second value to swap')
    parser.add_argument(
        '-m', '--method', 
        type=str, 
        choices=['tuple', 'arithmetic', 'xor', 'temp', 'all'],
        default='tuple',
        help='Swap method to use (default: tuple)'
    )
    parser.add_argument(
        '-v', '--verbose',
        action='store_true',
        help='Enable verbose output'
    )
    
    args = parser.parse_args()
    
    # Create swapper instance
    swapper = VariableSwapper(verbose=args.verbose)
    
    # Check if running in command-line mode or interactive mode
    if args.first is not None and args.second is not None:
        # Command-line mode
        logger.info(f"Running in command-line mode")
        
        # Detect types
        a, a_type = swapper.detect_type(args.first)
        b, b_type = swapper.detect_type(args.second)
        
        print(f"Input types: a={a_type.__name__}, b={b_type.__name__}")
        
        # Map method string to enum
        method_map = {
            'tuple': SwapMethod.TUPLE_UNPACKING,
            'arithmetic': SwapMethod.ARITHMETIC,
            'xor': SwapMethod.XOR,
            'temp': SwapMethod.TEMPORARY,
            'all': SwapMethod.ALL
        }
        
        selected_method = method_map[args.method]
        
        if selected_method == SwapMethod.ALL:
            # Try all methods
            methods = [SwapMethod.TUPLE_UNPACKING, SwapMethod.ARITHMETIC, 
                      SwapMethod.XOR, SwapMethod.TEMPORARY]
            for method in methods:
                result = swapper.perform_swap(a, b, method)
                display_result(result)
        else:
            # Use specific method
            result = swapper.perform_swap(a, b, selected_method)
            display_result(result)
            
            if not result.success:
                sys.exit(1)
    else:
        # Interactive mode
        logger.info("Running in interactive mode")
        interactive_mode(swapper)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nOperation cancelled by user.")
        sys.exit(0)
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        sys.exit(1)
