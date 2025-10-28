#!/usr/bin/env python3
"""swap_variables.py

Advanced module for demonstrating multiple variable swapping techniques in Python.

This module provides a comprehensive exploration of variable swapping in Python,
showcasing different approaches and their trade-offs. It serves both as an
educational tool and a practical utility for understanding Python's memory
management and variable assignment mechanisms.

OVERVIEW:
---------
Variable swapping is a fundamental programming operation where the values of
two variables are exchanged. While simple in concept, different implementation
methods reveal important aspects of a programming language's design.

METHODS IMPLEMENTED:
-------------------
1. Tuple Unpacking (Pythonic way)
   - Most readable and idiomatic in Python
   - Works with any data type
   - Time Complexity: O(1)
   - Space Complexity: O(1)
   
2. Arithmetic Operations
   - Uses mathematical properties
   - Limited to numeric types
   - Risk of overflow with very large numbers
   - Time Complexity: O(1)
   - Space Complexity: O(1)
   
3. XOR Bitwise Operation
   - Clever bit manipulation technique
   - Limited to integers
   - Fails if both variables reference the same object
   - Time Complexity: O(1)
   - Space Complexity: O(1)
   
4. Traditional Temporary Variable
   - Most universal approach across languages
   - Clear and explicit
   - Time Complexity: O(1)
   - Space Complexity: O(1)

FEATURES:
---------
- Type detection and automatic conversion
- Comprehensive error handling
- Multiple swap methods demonstration
- Command-line argument support for automation
- Logging capability for debugging
- Interactive menu system for exploration
- Performance comparison capabilities

USAGE EXAMPLES:
--------------
Interactive Mode:
    $ python swap_variables.py
    
Command-line Mode:
    $ python swap_variables.py -a 10 -b 20
    $ python swap_variables.py -a "hello" -b "world" -m tuple
    $ python swap_variables.py -a 42 -b 17 -m all -v
    
As a Module:
    >>> from swap_variables import VariableSwapper
    >>> swapper = VariableSwapper()
    >>> a, b = swapper.swap_tuple_unpacking(10, 20)
    >>> print(f"a={a}, b={b}")  # Output: a=20, b=10

TECHNICAL NOTES:
---------------
- Python's tuple unpacking creates a temporary tuple internally
- The XOR method works because: a^b^b = a and a^a^b = b
- Arithmetic method relies on: (a+b)-b = a and (a+b)-a = b
- All methods maintain object identity for immutable types

Author: [Your Name]
Date: [Current Date]
Python Version: 3.8+ (uses dataclasses, type hints, f-strings)
Dependencies: None (uses only standard library)
License: MIT
"""

import argparse
import logging
import sys
from enum import Enum
from typing import Any, Tuple, Optional, Union
from dataclasses import dataclass


# Configure logging with detailed format for debugging
# Format includes timestamp, logger name, level, and message
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class SwapMethod(Enum):
    """
    Enumeration of available swap methods.
    
    This enum provides a type-safe way to specify swap methods,
    preventing typos and enabling IDE autocomplete. Each value
    corresponds to a string identifier used in command-line arguments.
    
    Attributes:
        TUPLE_UNPACKING: Python's idiomatic tuple unpacking method
        ARITHMETIC: Mathematical approach using addition/subtraction
        XOR: Bitwise XOR operation method
        TEMPORARY: Traditional temporary variable approach
        ALL: Special value to indicate all methods should be demonstrated
    """
    TUPLE_UNPACKING = "tuple"    # Most Pythonic approach
    ARITHMETIC = "arithmetic"     # Mathematical manipulation
    XOR = "xor"                  # Bitwise operation
    TEMPORARY = "temp"           # Traditional approach
    ALL = "all"                  # Demonstrate all methods


@dataclass
class SwapResult:
    """
    Data class to store swap operation results.
    
    This immutable data structure encapsulates all information about
    a swap operation, including success status and error details.
    Using a dataclass provides automatic __init__, __repr__, and __eq__ methods.
    
    Attributes:
        original_a: The original value of the first variable
        original_b: The original value of the second variable
        swapped_a: The value of first variable after swapping
        swapped_b: The value of second variable after swapping
        method: String identifier of the swap method used
        success: Boolean indicating if swap was successful
        error_message: Optional error message if swap failed
        
    Example:
        >>> result = SwapResult(
        ...     original_a=10, original_b=20,
        ...     swapped_a=20, swapped_b=10,
        ...     method="tuple", success=True
        ... )
        >>> print(result.success)  # True
    """
    original_a: Any                      # Original first value (any type)
    original_b: Any                      # Original second value (any type)
    swapped_a: Any                       # First value after swap
    swapped_b: Any                       # Second value after swap
    method: str                          # Method name used for swap
    success: bool                        # Whether swap succeeded
    error_message: Optional[str] = None # Error details if swap failed


class VariableSwapper:
    """
    Class to handle various variable swapping operations.
    
    This class encapsulates all swap logic and provides a clean interface
    for performing different types of swaps. It includes type detection,
    error handling, and logging capabilities.
    
    The class design follows the Single Responsibility Principle by focusing
    solely on swap operations and related type detection.
    
    Attributes:
        verbose: Boolean flag for detailed logging output
        
    Methods:
        detect_type: Analyzes and converts string input to appropriate type
        swap_tuple_unpacking: Performs swap using Python tuple unpacking
        swap_arithmetic: Performs swap using arithmetic operations
        swap_xor: Performs swap using XOR bitwise operation
        swap_temporary: Performs swap using temporary variable
        perform_swap: Main method that delegates to specific swap method
        
    Example:
        >>> swapper = VariableSwapper(verbose=True)
        >>> result = swapper.perform_swap(10, 20, SwapMethod.TUPLE_UNPACKING)
        >>> print(result.swapped_a, result.swapped_b)  # 20 10
    """

    def __init__(self, verbose: bool = False):
        """
        Initialize the VariableSwapper.
        
        Sets up the swapper with optional verbose logging. When verbose
        mode is enabled, DEBUG level messages will be displayed, providing
        detailed information about the swap process.

        Args:
            verbose: If True, enables detailed DEBUG logging output.
                    Useful for understanding the internal swap process.
                    
        Example:
            >>> swapper = VariableSwapper(verbose=True)
            # Will show detailed logs during swap operations
        """
        self.verbose = verbose
        # Adjust logger level based on verbose flag
        if verbose:
            logger.setLevel(logging.DEBUG)
            logger.debug("VariableSwapper initialized in verbose mode")

    def detect_type(self, value: str) -> Tuple[Any, type]:
        """
        Detect and convert string input to appropriate Python type.
        
        This method attempts to intelligently convert string input to the
        most appropriate Python type. It tries conversions in order of
        specificity: int -> float -> bool -> str.
        
        The detection order is important:
        - Integer check must come before float (integers are valid floats)
        - Boolean check uses string matching for 'true'/'false'
        - String is the fallback for any non-convertible input

        Args:
            value: String value to analyze and convert
            
        Returns:
            Tuple containing:
                - Converted value in detected type
                - Python type object for the detected type
                
        Examples:
            >>> swapper = VariableSwapper()
            >>> swapper.detect_type("42")
            (42, <class 'int'>)
            >>> swapper.detect_type("3.14")
            (3.14, <class 'float'>)
            >>> swapper.detect_type("true")
            (True, <class 'bool'>)
            >>> swapper.detect_type("hello")
            ('hello', <class 'str'>)
        """
        # Try integer conversion first (most specific numeric type)
        try:
            # int() will raise ValueError if string contains non-numeric chars
            converted_value = int(value)
            logger.debug(f"Detected integer type for value: {value}")
            return converted_value, int
        except ValueError:
            # Not an integer, continue to next type
            pass

        # Try float conversion (less specific than int)
        try:
            # float() accepts integers and floats, but not non-numeric strings
            converted_value = float(value)
            logger.debug(f"Detected float type for value: {value}")
            return converted_value, float
        except ValueError:
            # Not a float, continue to next type
            pass

        # Check for boolean values (case-insensitive)
        # Only 'true' and 'false' strings are considered booleans
        if value.lower() in ('true', 'false'):
            converted_value = value.lower() == 'true'
            logger.debug(f"Detected boolean type for value: {value}")
            return converted_value, bool

        # Default to string type (no conversion needed)
        # This is the fallback for any value that doesn't match above types
        logger.debug(f"Defaulting to string type for value: {value}")
        return value, str

    def swap_tuple_unpacking(self, a: Any, b: Any) -> Tuple[Any, Any]:
        """
        Swap using Python's tuple unpacking method.
        
        This is the most Pythonic and recommended way to swap variables.
        It leverages Python's ability to create and unpack tuples in a
        single expression. Internally, Python creates a temporary tuple
        (b, a) and then unpacks it to assign values.
        
        How it works:
        1. Right side (b, a) creates a tuple with swapped order
        2. Left side unpacks this tuple into variables
        3. Assignment happens simultaneously (atomic operation)
        
        Advantages:
        - Most readable and Pythonic
        - Works with any data type
        - No risk of overflow or type issues
        - Thread-safe (atomic operation)
        
        Args:
            a: First value of any type
            b: Second value of any type
            
        Returns:
            Tuple of swapped values (b, a)
            
        Example:
            >>> swapper = VariableSwapper()
            >>> x, y = swapper.swap_tuple_unpacking(10, 20)
            >>> print(x, y)  # 20 10
        """
        logger.debug(f"Swapping {a!r} and {b!r} using tuple unpacking")
        # Python creates tuple (b, a) then unpacks it
        # This is equivalent to: temp = (b, a); return temp[0], temp[1]
        return b, a

    def swap_arithmetic(self, a: Union[int, float], b: Union[int, float]) -> Tuple[Union[int, float], Union[int, float]]:
        """
        Swap using arithmetic operations (works only with numbers).
        
        This method uses mathematical properties to swap without explicit
        temporary storage. It works by encoding both values in their sum,
        then extracting each value through subtraction.
        
        Mathematical proof:
        1. a = a + b  (a now contains sum of both)
        2. b = a - b  (b = (a+b) - b = original a)
        3. a = a - b  (a = (a+b) - original_a = original b)
        
        Limitations:
        - Only works with numeric types (int, float)
        - Risk of overflow with very large numbers
        - Potential precision loss with floating-point numbers
        - Cannot swap if a and b reference the same variable
        
        Args:
            a: First numeric value (int or float)
            b: Second numeric value (int or float)
            
        Returns:
            Tuple of swapped numeric values
            
        Raises:
            TypeError: If values are not numeric (int or float)
            
        Example:
            >>> swapper = VariableSwapper()
            >>> x, y = swapper.swap_arithmetic(10, 20)
            >>> print(x, y)  # 20 10
        """
        # Type checking to ensure numeric values
        if not all(isinstance(x, (int, float)) for x in [a, b]):
            raise TypeError("Arithmetic swap requires numeric values")
        
        logger.debug(f"Swapping {a} and {b} using arithmetic method")
        
        # Step 1: Store sum in 'a'
        a = a + b  # a now contains the sum of original values
        
        # Step 2: Extract original 'a' value into 'b'
        b = a - b  # b = (original_a + original_b) - original_b = original_a
        
        # Step 3: Extract original 'b' value into 'a'
        a = a - b  # a = (original_a + original_b) - original_a = original_b
        
        return a, b

    def swap_xor(self, a: int, b: int) -> Tuple[int, int]:
        """
        Swap using XOR bitwise operation (works only with integers).
        
        This method uses the XOR operation's properties to swap values
        without additional storage. XOR is its own inverse operation.
        
        XOR Truth Table:
        0 ^ 0 = 0    1 ^ 0 = 1
        0 ^ 1 = 1    1 ^ 1 = 0
        
        Mathematical properties used:
        - a ^ b ^ b = a (XOR with same value twice returns original)
        - a ^ a = 0 (XOR of identical values is zero)
        - a ^ 0 = a (XOR with zero returns original)
        
        How it works:
        1. a = a ^ b  (a stores XOR combination)
        2. b = a ^ b = (a^b) ^ b = a (extracts original a)
        3. a = a ^ b = (a^b) ^ a = b (extracts original b)
        
        Limitations:
        - Only works with integers
        - Fails if a and b reference the same memory location
        - Not intuitive to understand
        
        Performance note: Despite no temp variable, modern CPUs may
        execute tuple unpacking faster due to instruction pipelining.
        
        Args:
            a: First integer value
            b: Second integer value
            
        Returns:
            Tuple of swapped integer values
            
        Raises:
            TypeError: If values are not integers
            
        Example:
            >>> swapper = VariableSwapper()
            >>> x, y = swapper.swap_xor(10, 20)
            >>> print(x, y)  # 20 10
        """
        # Ensure both values are integers for bitwise operations
        if not all(isinstance(x, int) for x in [a, b]):
            raise TypeError("XOR swap requires integer values")
        
        logger.debug(f"Swapping {a} and {b} using XOR method")
        logger.debug(f"Binary: a={bin(a)}, b={bin(b)}")
        
        # Step 1: Combine both values using XOR
        a = a ^ b  # a now contains XOR of both original values
        logger.debug(f"After a^b: a={bin(a)}")
        
        # Step 2: Extract original 'a' into 'b'
        b = a ^ b  # b = (a^b) ^ b = a^(b^b) = a^0 = a
        logger.debug(f"After (a^b)^b: b={bin(b)}")
        
        # Step 3: Extract original 'b' into 'a'
        a = a ^ b  # a = (a^b) ^ a = (a^b)^a = b^(a^a) = b^0 = b
        logger.debug(f"After (a^b)^a: a={bin(a)}")
        
        return a, b

    def swap_temporary(self, a: Any, b: Any) -> Tuple[Any, Any]:
        """
        Swap using traditional temporary variable method.
        
        This is the most universal and straightforward approach, used
        in most programming languages. It explicitly stores one value
        in a temporary variable during the swap process.
        
        This method is:
        - Most portable across languages
        - Easiest to understand for beginners
        - Safest (no edge cases or type restrictions)
        - Clear in its intent
        
        Memory usage: Creates one additional reference, but Python's
        garbage collector handles this efficiently.
        
        Args:
            a: First value of any type
            b: Second value of any type
            
        Returns:
            Tuple of swapped values
            
        Example:
            >>> swapper = VariableSwapper()
            >>> x, y = swapper.swap_temporary([1,2], [3,4])
            >>> print(x, y)  # [3,4] [1,2]
        """
        logger.debug(f"Swapping {a!r} and {b!r} using temporary variable")
        
        # Step 1: Store first value in temporary variable
        temp = a  # Preserve original value of 'a'
        
        # Step 2: Assign second value to first variable
        a = b     # 'a' now has the value of 'b'
        
        # Step 3: Assign temporary (original first) to second variable
        b = temp  # 'b' now has the original value of 'a'
        
        return a, b

    def perform_swap(self, a: Any, b: Any, method: SwapMethod) -> SwapResult:
        """
        Perform swap operation using specified method.
        
        This is the main orchestrator method that delegates to the appropriate
        swap implementation based on the selected method. It handles errors
        gracefully and returns a comprehensive result object.
        
        The method:
        1. Stores original values for comparison
        2. Attempts the requested swap operation
        3. Catches any errors (type mismatches, etc.)
        4. Returns a SwapResult with all details
        
        Args:
            a: First value to swap
            b: Second value to swap
            method: SwapMethod enum indicating which swap method to use
            
        Returns:
            SwapResult object containing:
                - Original values
                - Swapped values (if successful)
                - Success status
                - Error message (if failed)
                
        Example:
            >>> swapper = VariableSwapper()
            >>> result = swapper.perform_swap(10, 20, SwapMethod.TUPLE_UNPACKING)
            >>> if result.success:
            ...     print(f"Swapped: {result.swapped_a}, {result.swapped_b}")
        """
        # Preserve original values for result object
        original_a, original_b = a, b
        
        try:
            # Dispatch to appropriate swap method based on enum
            if method == SwapMethod.TUPLE_UNPACKING:
                a, b = self.swap_tuple_unpacking(a, b)
                
            elif method == SwapMethod.ARITHMETIC:
                # May raise TypeError for non-numeric types
                a, b = self.swap_arithmetic(a, b)
                
            elif method == SwapMethod.XOR:
                # May raise TypeError for non-integer types
                a, b = self.swap_xor(a, b)
                
            elif method == SwapMethod.TEMPORARY:
                a, b = self.swap_temporary(a, b)
                
            # Create successful result object
            return SwapResult(
                original_a=original_a,
                original_b=original_b,
                swapped_a=a,
                swapped_b=b,
                method=method.value,
                success=True
            )
            
        except (TypeError, ValueError) as e:
            # Log error for debugging
            logger.error(f"Swap failed: {e}")
            
            # Return failure result with error details
            return SwapResult(
                original_a=original_a,
                original_b=original_b,
                swapped_a=original_a,  # Keep original values on failure
                swapped_b=original_b,
                method=method.value,
                success=False,
                error_message=str(e)
            )


def display_result(result: SwapResult) -> None:
    """
    Display swap operation result in formatted output.
    
    This function provides a user-friendly display of swap results,
    showing before/after values or error messages as appropriate.
    It uses Unicode characters for better visual presentation.
    
    Output format:
    - Header with method name
    - Before/after values if successful
    - Error message with ❌ emoji if failed
    
    Args:
        result: SwapResult object to display
        
    Example:
        >>> result = SwapResult(
        ...     original_a=10, original_b=20,
        ...     swapped_a=20, swapped_b=10,
        ...     method="tuple", success=True
        ... )
        >>> display_result(result)
        ==================================================
        Method: TUPLE
        ==================================================
        Before swapping: a = 10, b = 20
        After swapping:  a = 20, b = 10
    """
    # Create visual separator with method name
    print(f"\n{'='*50}")
    print(f"Method: {result.method.upper()}")
    print(f"{'='*50}")
    
    if result.success:
        # Display successful swap with aligned output
        print(f"Before swapping: a = {result.original_a}, b = {result.original_b}")
        print(f"After swapping:  a = {result.swapped_a}, b = {result.swapped_b}")
    else:
        # Display error with visual indicator
        print(f"❌ Swap failed: {result.error_message}")


def interactive_mode(swapper: VariableSwapper) -> None:
    """
    Run interactive mode with menu-driven interface.
    
    This function provides a user-friendly interactive interface for
    exploring different swap methods. It includes:
    - Input validation
    - Type detection and display
    - Method selection menu
    - Option to try all methods
    - Continuous operation until user exits
    
    The interface is designed to be educational, showing type detection
    results and allowing experimentation with different methods.
    
    Args:
        swapper: VariableSwapper instance to use for operations
        
    Flow:
    1. Prompt for two values (with exit option)
    2. Detect and display types
    3. Show method selection menu
    4. Perform selected swap(s)
    5. Display results
    6. Ask to continue or exit
    """
    while True:
        # Display header for new swap operation
        print("\n" + "="*60)
        print("VARIABLE SWAPPER - INTERACTIVE MODE")
        print("="*60)
        
        # Get first value with exit option
        a_str = input("\nEnter the value of variable a (or 'quit' to exit): ").strip()
        
        # Check for exit command
        if a_str.lower() == 'quit':
            print("Goodbye!")
            break
            
        # Get second value
        b_str = input("Enter the value of variable b: ").strip()
        
        # Perform type detection and conversion
        a, a_type = swapper.detect_type(a_str)
        b, b_type = swapper.detect_type(b_str)
        
        # Display detected types for educational purposes
        print(f"\nDetected types: a={a_type.__name__}, b={b_type.__name__}")
        
        # Display menu with method descriptions
        print("\nSelect swap method:")
        print("1. Tuple Unpacking (works with all types)")
        print("2. Arithmetic (numbers only)")
        print("3. XOR Bitwise (integers only)")
        print("4. Temporary Variable (works with all types)")
        print("5. Demonstrate All Methods")
        
        # Get user choice with validation
        choice = input("\nEnter your choice (1-5): ").strip()
        
        # Map numeric choice to SwapMethod enum
        method_map = {
            '1': SwapMethod.TUPLE_UNPACKING,
            '2': SwapMethod.ARITHMETIC,
            '3': SwapMethod.XOR,
            '4': SwapMethod.TEMPORARY,
            '5': SwapMethod.ALL
        }
        
        # Validate choice
        if choice not in method_map:
            print("❌ Invalid choice!")
            continue
        
        selected_method = method_map[choice]
        
        # Perform swap operation(s)
        if selected_method == SwapMethod.ALL:
            # Demonstrate all methods for comparison
            methods = [SwapMethod.TUPLE_UNPACKING, SwapMethod.ARITHMETIC, 
                      SwapMethod.XOR, SwapMethod.TEMPORARY]
            for method in methods:
                result = swapper.perform_swap(a, b, method)
                display_result(result)
        else:
            # Perform single selected method
            result = swapper.perform_swap(a, b, selected_method)
            display_result(result)
        
        # Ask user if they want to continue
        if input("\nDo you want to swap more variables? (y/n): ").lower() != 'y':
            print("Thank you for using Variable Swapper!")
            break


def main() -> None:
    """
    Main entry point with CLI and interactive support.
    
    This function serves as the program entry point, providing:
    1. Command-line argument parsing for automation
    2. Interactive mode for exploration
    3. Error handling for graceful exit
    4. Logging configuration
    
    The dual-mode design allows the program to be used:
    - As a command-line tool for scripts and automation
    - As an interactive educational tool
    - As an importable module for other programs
    
    Command-line arguments:
        -a, --first: First value to swap
        -b, --second: Second value to swap
        -m, --method: Swap method to use
        -v, --verbose: Enable verbose logging
        
    Exit codes:
        0: Successful execution
        1: Error during execution
        
    Examples:
        Interactive mode:
            $ python swap_variables.py
            
        Command-line mode:
            $ python swap_variables.py -a 10 -b 20
            $ python swap_variables.py -a hello -b world -m tuple -v
    """
    # Create argument parser with detailed help
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
    
    # Define command-line arguments
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
    
    # Parse command-line arguments
    args = parser.parse_args()
    
    # Initialize swapper with verbose flag
    swapper = VariableSwapper(verbose=args.verbose)
    
    # Determine execution mode based on provided arguments
    if args.first is not None and args.second is not None:
        # Command-line mode - both values provided
        logger.info(f"Running in command-line mode")
        
        # Detect and convert input types
        a, a_type = swapper.detect_type(args.first)
        b, b_type = swapper.detect_type(args.second)
        
        # Display detected types
        print(f"Input types: a={a_type.__name__}, b={b_type.__name__}")
        
        # Map method string to enum value
        method_map = {
            'tuple': SwapMethod.TUPLE_UNPACKING,
            'arithmetic': SwapMethod.ARITHMETIC,
            'xor': SwapMethod.XOR,
            'temp': SwapMethod.TEMPORARY,
            'all': SwapMethod.ALL
        }
        
        selected_method = method_map[args.method]
        
        if selected_method == SwapMethod.ALL:
            # Demonstrate all available methods
            methods = [SwapMethod.TUPLE_UNPACKING, SwapMethod.ARITHMETIC, 
                      SwapMethod.XOR, SwapMethod.TEMPORARY]
            for method in methods:
                result = swapper.perform_swap(a, b, method)
                display_result(result)
        else:
            # Use specifically requested method
            result = swapper.perform_swap(a, b, selected_method)
            display_result(result)
            
            # Exit with error code if swap failed
            if not result.success:
                sys.exit(1)
    else:
        # Interactive mode - no values provided via CLI
        logger.info("Running in interactive mode")
        interactive_mode(swapper)


# Module execution guard
# Ensures main() only runs when script is executed directly,
# not when imported as a module
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        # Handle Ctrl+C gracefully
        print("\n\nOperation cancelled by user.")
        sys.exit(0)
    except Exception as e:
        # Log unexpected errors and exit with error code
        logger.error(f"Unexpected error: {e}")
        sys.exit(1)
