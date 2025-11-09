#!/usr/bin/env python3
"""positive_negative.py

Advanced number classification and analysis system.

This module provides comprehensive number analysis including:
- Sign classification (positive, negative, zero)
- Mathematical properties (prime, perfect, fibonacci, etc.)
- Statistical analysis for number sets
- Visualization with ASCII charts
- Pattern recognition
- Number system conversions
- Mathematical constants comparison

Features:
    - Multiple classification algorithms
    - Batch processing with statistics
    - Interactive and CLI modes
    - Data export (JSON, CSV)
    - ASCII visualization
    - Performance benchmarking
    - Educational explanations

Author: [Your Name]
Date: [Current Date]
Python Version: 3.8+
"""

import argparse
import json
import csv
import sys
import math
import time
import statistics
from typing import Union, List, Dict, Any, Tuple, Optional, Callable
from dataclasses import dataclass, asdict
from enum import Enum, auto
from collections import Counter, defaultdict
from functools import lru_cache
import random


class NumberType(Enum):
    """Enumeration of number sign types."""
    POSITIVE = "Positive"
    NEGATIVE = "Negative"
    ZERO = "Zero"


class SpecialProperty(Enum):
    """Enumeration of special number properties."""
    PRIME = auto()
    PERFECT = auto()
    FIBONACCI = auto()
    PALINDROME = auto()
    ARMSTRONG = auto()
    HAPPY = auto()
    TRIANGULAR = auto()
    SQUARE = auto()
    CUBE = auto()
    FACTORIAL = auto()


@dataclass
class NumberAnalysis:
    """Comprehensive analysis results for a number."""
    value: float
    sign: str
    absolute_value: float
    integer_part: int
    fractional_part: float
    is_integer: bool
    is_even: Optional[bool]
    is_odd: Optional[bool]
    binary: Optional[str]
    hexadecimal: Optional[str]
    octal: Optional[str]
    scientific_notation: str
    special_properties: List[str]
    nearest_integer: int
    reciprocal: Optional[float]
    square: float
    square_root: float
    cube: float
    cube_root: float
    logarithm_base10: Optional[float]
    logarithm_natural: Optional[float]
    sine: float
    cosine: float
    factors: Optional[List[int]]
    digit_sum: Optional[int]
    digit_product: Optional[int]
    comparison_to_constants: Dict[str, str]


@dataclass
class BatchStatistics:
    """Statistics for batch number processing."""
    count: int
    positive_count: int
    negative_count: int
    zero_count: int
    mean: float
    median: float
    mode: Optional[float]
    std_dev: float
    variance: float
    minimum: float
    maximum: float
    range: float
    sum: float
    geometric_mean: Optional[float]
    harmonic_mean: Optional[float]
    quartiles: Tuple[float, float, float]
    outliers: List[float]


class NumberClassifier:
    """Advanced number classification and analysis system."""
    
    # Mathematical constants for comparison
    CONSTANTS = {
        'π (pi)': math.pi,
        'e (Euler)': math.e,
        'φ (golden ratio)': (1 + math.sqrt(5)) / 2,
        '√2': math.sqrt(2),
        '√3': math.sqrt(3),
        'ln(2)': math.log(2),
        'ln(10)': math.log(10),
    }
    
    def __init__(self, verbose: bool = False, precision: int = 6):
        """
        Initialize the NumberClassifier.
        
        Args:
            verbose: Enable detailed output
            precision: Decimal precision for floating-point operations
        """
        self.verbose = verbose
        self.precision = precision
        self.analysis_history: List[NumberAnalysis] = []
    
    def check_number(self, num: Union[int, float]) -> str:
        """
        Determine if a number is positive, negative, or zero.
        
        Args:
            num: A numeric value to check
            
        Returns:
            Classification as string
        """
        if num > 0:
            return NumberType.POSITIVE.value
        elif num < 0:
            return NumberType.NEGATIVE.value
        else:
            return NumberType.ZERO.value
    
    @lru_cache(maxsize=128)
    def is_prime(self, n: int) -> bool:
        """Check if a number is prime."""
        if n < 2:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        for i in range(3, int(math.sqrt(n)) + 1, 2):
            if n % i == 0:
                return False
        return True
    
    def is_perfect(self, n: int) -> bool:
        """Check if a number is perfect (sum of divisors equals the number)."""
        if n <= 0:
            return False
        divisor_sum = sum(i for i in range(1, n) if n % i == 0)
        return divisor_sum == n
    
    @lru_cache(maxsize=128)
    def is_fibonacci(self, n: int) -> bool:
        """Check if a number is in the Fibonacci sequence."""
        if n < 0:
            return False
        # A number is Fibonacci if one of 5n²+4 or 5n²-4 is a perfect square
        def is_perfect_square(x):
            root = int(math.sqrt(x))
            return root * root == x
        return is_perfect_square(5 * n * n + 4) or is_perfect_square(5 * n * n - 4)
    
    def is_palindrome(self, n: float) -> bool:
        """Check if a number is a palindrome."""
        s = str(abs(n)).replace('.', '').replace('-', '')
        return s == s[::-1]
    
    def is_armstrong(self, n: int) -> bool:
        """Check if a number is an Armstrong number."""
        if n < 0:
            return False
        digits = [int(d) for d in str(n)]
        power = len(digits)
        return sum(d ** power for d in digits) == n
    
    def is_happy(self, n: int) -> bool:
        """Check if a number is a happy number."""
        def sum_of_squares(num):
            return sum(int(digit) ** 2 for digit in str(num))
        
        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            n = sum_of_squares(n)
        return n == 1
    
    def get_factors(self, n: int) -> List[int]:
        """Get all factors of a number."""
        if n == 0:
            return []
        n = abs(n)
        factors = []
        for i in range(1, int(math.sqrt(n)) + 1):
            if n % i == 0:
                factors.append(i)
                if i != n // i:
                    factors.append(n // i)
        return sorted(factors)
    
    def analyze_number(self, num: Union[int, float]) -> NumberAnalysis:
        """
        Perform comprehensive analysis on a number.
        
        Args:
            num: Number to analyze
            
        Returns:
            NumberAnalysis object with complete analysis
        """
        # Basic properties
        sign = self.check_number(num)
        abs_val = abs(num)
        int_part = int(num)
        frac_part = num - int_part
        is_int = isinstance(num, int) or num.is_integer()
        
        # Integer-specific properties
        if is_int:
            int_num = int(num)
            is_even = int_num % 2 == 0
            is_odd = not is_even
            binary = bin(int(abs_val))
            hexadecimal = hex(int(abs_val))
            octal = oct(int(abs_val))
            factors = self.get_factors(int_num) if int_num != 0 else None
            digit_sum = sum(int(d) for d in str(abs(int_num)))
            digit_product = math.prod(int(d) for d in str(abs(int_num)))
        else:
            is_even = is_odd = None
            binary = hexadecimal = octal = None
            factors = None
            digit_sum = digit_product = None
        
        # Special properties
        special_props = []
        if is_int and abs(int_num) > 0:
            if self.is_prime(abs(int_num)):
                special_props.append("Prime")
            if self.is_perfect(abs(int_num)):
                special_props.append("Perfect")
            if self.is_fibonacci(abs(int_num)):
                special_props.append("Fibonacci")
            if self.is_armstrong(abs(int_num)):
                special_props.append("Armstrong")
            if self.is_happy(abs(int_num)):
                special_props.append("Happy")
        
        if self.is_palindrome(num):
            special_props.append("Palindrome")
        
        # Mathematical operations
        reciprocal = 1/num if num != 0 else None
        square = num ** 2
        square_root = math.sqrt(abs_val)
        cube = num ** 3
        cube_root = abs_val ** (1/3) if num >= 0 else -(abs_val ** (1/3))
        
        # Logarithms
        log10 = math.log10(abs_val) if num > 0 else None
        ln = math.log(abs_val) if num > 0 else None
        
        # Trigonometry
        sine = math.sin(num)
        cosine = math.cos(num)
        
        # Compare to mathematical constants
        comparisons = {}
        for name, const in self.CONSTANTS.items():
            if abs(num - const) < 0.0001:
                comparisons[name] = "≈ equal"
            elif num < const:
                comparisons[name] = "less than"
            else:
                comparisons[name] = "greater than"
        
        analysis = NumberAnalysis(
            value=num,
            sign=sign,
            absolute_value=abs_val,
            integer_part=int_part,
            fractional_part=frac_part,
            is_integer=is_int,
            is_even=is_even,
            is_odd=is_odd,
            binary=binary,
            hexadecimal=hexadecimal,
            octal=octal,
            scientific_notation=f"{num:.2e}",
            special_properties=special_props,
            nearest_integer=round(num),
            reciprocal=reciprocal,
            square=square,
            square_root=square_root,
            cube=cube,
            cube_root=cube_root,
            logarithm_base10=log10,
            logarithm_natural=ln,
            sine=sine,
            cosine=cosine,
            factors=factors,
            digit_sum=digit_sum,
            digit_product=digit_product,
            comparison_to_constants=comparisons
        )
        
        self.analysis_history.append(analysis)
        return analysis
    
    def analyze_batch(self, numbers: List[Union[int, float]]) -> BatchStatistics:
        """
        Analyze a batch of numbers and compute statistics.
        
        Args:
            numbers: List of numbers to analyze
            
        Returns:
            BatchStatistics object
        """
        if not numbers:
            raise ValueError("Cannot analyze empty list")
        
        # Count by sign
        positive = sum(1 for n in numbers if n > 0)
        negative = sum(1 for n in numbers if n < 0)
        zero = sum(1 for n in numbers if n == 0)
        
        # Basic statistics
        mean = statistics.mean(numbers)
        median = statistics.median(numbers)
        
        # Mode (if exists)
        try:
            mode = statistics.mode(numbers)
        except statistics.StatisticsError:
            mode = None
        
        # Variation measures
        if len(numbers) > 1:
            std_dev = statistics.stdev(numbers)
            variance = statistics.variance(numbers)
        else:
            std_dev = variance = 0
        
        # Range
        minimum = min(numbers)
        maximum = max(numbers)
        range_val = maximum - minimum
        
        # Advanced means
        positive_nums = [n for n in numbers if n > 0]
        if positive_nums:
            geometric_mean = statistics.geometric_mean(positive_nums)
            harmonic_mean = statistics.harmonic_mean(positive_nums)
        else:
            geometric_mean = harmonic_mean = None
        
        # Quartiles
        sorted_nums = sorted(numbers)
        q1 = statistics.quantiles(sorted_nums, n=4)[0]
        q2 = median
        q3 = statistics.quantiles(sorted_nums, n=4)[2]
        
        # Detect outliers using IQR method
        iqr = q3 - q1
        lower_bound = q1 - 1.5 * iqr
        upper_bound = q3 + 1.5 * iqr
        outliers = [n for n in numbers if n < lower_bound or n > upper_bound]
        
        return BatchStatistics(
            count=len(numbers),
            positive_count=positive,
            negative_count=negative,
            zero_count=zero,
            mean=mean,
            median=median,
            mode=mode,
            std_dev=std_dev,
            variance=variance,
            minimum=minimum,
            maximum=maximum,
            range=range_val,
            sum=sum(numbers),
            geometric_mean=geometric_mean,
            harmonic_mean=harmonic_mean,
            quartiles=(q1, q2, q3),
            outliers=outliers
        )
    
    def visualize_distribution(self, numbers: List[Union[int, float]], bins: int = 10) -> str:
        """
        Create ASCII histogram of number distribution.
        
        Args:
            numbers: List of numbers
            bins: Number of bins for histogram
            
        Returns:
            ASCII histogram string
        """
        if not numbers:
            return "No data to visualize"
        
        # Create histogram
        min_val, max_val = min(numbers), max(numbers)
        if min_val == max_val:
            return f"All values are {min_val}"
        
        bin_width = (max_val - min_val) / bins
        histogram = defaultdict(int)
        
        for num in numbers:
            bin_idx = min(int((num - min_val) / bin_width), bins - 1)
            histogram[bin_idx] += 1
        
        # Find max count for scaling
        max_count = max(histogram.values())
        bar_width = 40
        
        # Build visualization
        result = ["\n📊 Distribution Histogram:\n" + "="*50]
        
        for i in range(bins):
            bin_start = min_val + i * bin_width
            bin_end = bin_start + bin_width
            count = histogram[i]
            bar_length = int((count / max_count) * bar_width) if max_count > 0 else 0
            bar = "█" * bar_length
            
            result.append(f"[{bin_start:7.2f} - {bin_end:7.2f}] {bar} {count}")
        
        # Add sign distribution pie chart
        positive = sum(1 for n in numbers if n > 0)
        negative = sum(1 for n in numbers if n < 0)
        zero = sum(1 for n in numbers if n == 0)
        total = len(numbers)
        
        result.append("\n📈 Sign Distribution:")
        result.append("="*50)
        if positive:
            result.append(f"Positive: {'+'*int(40*positive/total)} {positive}/{total} ({100*positive/total:.1f}%)")
        if negative:
            result.append(f"Negative: {'-'*int(40*negative/total)} {negative}/{total} ({100*negative/total:.1f}%)")
        if zero:
            result.append(f"Zero:     {'0'*int(40*zero/total)} {zero}/{total} ({100*zero/total:.1f}%)")
        
        return "\n".join(result)
    
    def export_analysis(self, filename: str, format: str = "json") -> None:
        """
        Export analysis history to file.
        
        Args:
            filename: Output filename
            format: Export format ('json' or 'csv')
        """
        if not self.analysis_history:
            print("No analysis history to export")
            return
        
        if format == "json":
            with open(filename, 'w') as f:
                data = [asdict(a) for a in self.analysis_history]
                json.dump(data, f, indent=2, default=str)
        elif format == "csv":
            with open(filename, 'w', newline='') as f:
                if self.analysis_history:
                    fieldnames = asdict(self.analysis_history[0]).keys()
                    writer = csv.DictWriter(f, fieldnames=fieldnames)
                    writer.writeheader()
                    for analysis in self.analysis_history:
                        writer.writerow(asdict(analysis))
        
        print(f"✅ Analysis exported to {filename}")


def display_analysis(analysis: NumberAnalysis, detailed: bool = True) -> None:
    """
    Display number analysis results.
    
    Args:
        analysis: NumberAnalysis object
        detailed: Show all details
    """
    print("\n" + "="*60)
    print(f"📊 ANALYSIS OF {analysis.value}")
    print("="*60)
    
    # Basic classification
    print(f"\n🔍 Basic Properties:")
    print(f"  • Sign: {analysis.sign}")
    print(f"  • Absolute Value: {analysis.absolute_value}")
    print(f"  • Scientific Notation: {analysis.scientific_notation}")
    
    if analysis.is_integer:
        print(f"  • Type: Integer")
        print(f"  • Even/Odd: {'Even' if analysis.is_even else 'Odd'}")
    else:
        print(f"  • Type: Decimal")
        print(f"  • Integer Part: {analysis.integer_part}")
        print(f"  • Fractional Part: {analysis.fractional_part:.6f}")
    
    if detailed:
        # Number systems
        if analysis.binary:
            print(f"\n💻 Number Systems:")
            print(f"  • Binary: {analysis.binary}")
            print(f"  • Hexadecimal: {analysis.hexadecimal}")
            print(f"  • Octal: {analysis.octal}")
        
        # Mathematical operations
        print(f"\n🧮 Mathematical Operations:")
        print(f"  • Square: {analysis.square}")
        print(f"  • Square Root: {analysis.square_root:.6f}")
        print(f"  • Cube: {analysis.cube}")
        print(f"  • Cube Root: {analysis.cube_root:.6f}")
        if analysis.reciprocal:
            print(f"  • Reciprocal: {analysis.reciprocal:.6f}")
        
        # Special properties
        if analysis.special_properties:
            print(f"\n⭐ Special Properties:")
            for prop in analysis.special_properties:
                print(f"  • {prop}")
        
        # Factors
        if analysis.factors and len(analysis.factors) <= 20:
            print(f"\n🔢 Factors: {analysis.factors}")
        elif analysis.factors:
            print(f"\n🔢 Number of Factors: {len(analysis.factors)}")
        
        # Constants comparison
        print(f"\n📐 Comparison to Mathematical Constants:")
        for const, comparison in list(analysis.comparison_to_constants.items())[:3]:
            print(f"  • {const}: {comparison}")


def interactive_mode(classifier: NumberClassifier) -> None:
    """Run interactive mode with menu system."""
    while True:
        print("\n" + "="*60)
        print("🔢 ADVANCED NUMBER CLASSIFIER")
        print("="*60)
        print("\n1. Analyze Single Number")
        print("2. Analyze Multiple Numbers")
        print("3. Generate Random Numbers for Analysis")
        print("4. View Analysis History")
        print("5. Export Analysis History")
        print("6. Benchmark Performance")
        print("7. Educational Mode")
        print("8. Quit")
        
        choice = input("\nSelect option (1-8): ").strip()
        
        if choice == '1':
            try:
                num = float(input("\nEnter a number: "))
                analysis = classifier.analyze_number(num)
                display_analysis(analysis)
            except ValueError:
                print("❌ Invalid number")
        
        elif choice == '2':
            try:
                nums_str = input("\nEnter numbers separated by spaces: ")
                numbers = [float(n) for n in nums_str.split()]
                
                # Individual analysis
                for num in numbers:
                    analysis = classifier.analyze_number(num)
                    display_analysis(analysis, detailed=False)
                
                # Batch statistics
                stats = classifier.analyze_batch(numbers)
                print("\n" + "="*60)
                print("📈 BATCH STATISTICS")
                print("="*60)
                print(f"Count: {stats.count}")
                print(f"Mean: {stats.mean:.4f}")
                print(f"Median: {stats.median:.4f}")
                print(f"Std Dev: {stats.std_dev:.4f}")
                print(f"Range: [{stats.minimum}, {stats.maximum}]")
                
                # Visualization
                print(classifier.visualize_distribution(numbers))
                
            except ValueError:
                print("❌ Invalid input")
        
        elif choice == '3':
            try:
                count = int(input("How many random numbers? "))
                min_val = float(input("Minimum value: "))
                max_val = float(input("Maximum value: "))
                
                numbers = [random.uniform(min_val, max_val) for _ in range(count)]
                stats = classifier.analyze_batch(numbers)
                
                print(f"\n✅ Generated {count} random numbers")
                print(classifier.visualize_distribution(numbers))
                
            except ValueError:
                print("❌ Invalid input")
        
        elif choice == '4':
            if classifier.analysis_history:
                print(f"\n📋 Analysis History ({len(classifier.analysis_history)} items):")
                for i, analysis in enumerate(classifier.analysis_history[-5:], 1):
                    print(f"{i}. {analysis.value} → {analysis.sign}")
            else:
                print("No analysis history")
        
        elif choice == '5':
            if classifier.analysis_history:
                filename = input("Enter filename (without extension): ")
                format_choice = input("Format (json/csv): ").lower()
                if format_choice in ['json', 'csv']:
                    classifier.export_analysis(f"{filename}.{format_choice}", format_choice)
                else:
                    print("❌ Invalid format")
            else:
                print("No analysis history to export")
        
        elif choice == '6':
            print("\n⏱️ Benchmarking...")
            test_num = 12345
            
            start = time.perf_counter()
            for _ in range(10000):
                classifier.check_number(test_num)
            basic_time = time.perf_counter() - start
            
            start = time.perf_counter()
            for _ in range(1000):
                classifier.analyze_number(test_num)
            full_time = time.perf_counter() - start
            
            print(f"Basic check (10000x): {basic_time:.4f}s")
            print(f"Full analysis (1000x): {full_time:.4f}s")
        
        elif choice == '7':
            print("\n📚 EDUCATIONAL MODE")
            print("="*60)
            print("This program classifies numbers as positive, negative, or zero.")
            print("\nKey Concepts:")
            print("• Positive numbers: Greater than zero (n > 0)")
            print("• Negative numbers: Less than zero (n < 0)")
            print("• Zero: Neither positive nor negative (n = 0)")
            print("\nSpecial Number Types:")
            print("• Prime: Only divisible by 1 and itself")
            print("• Perfect: Sum of divisors equals the number")
            print("• Fibonacci: Part of the sequence 0,1,1,2,3,5,8...")
            print("• Armstrong: Sum of digits raised to power equals number")
        
        elif choice == '8':
            print("👋 Goodbye!")
            break
        
        else:
            print("❌ Invalid choice")


def main() -> None:
    """
    Main function with CLI support.
    """
    parser = argparse.ArgumentParser(
        description="Advanced number classification and analysis",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    
    parser.add_argument('numbers', nargs='*', type=float, help='Numbers to analyze')
    parser.add_argument('-d', '--detailed', action='store_true', help='Detailed analysis')
    parser.add_argument('-b', '--batch', action='store_true', help='Batch statistics')
    parser.add_argument('-v', '--visualize', action='store_true', help='Visualize distribution')
    parser.add_argument('-e', '--export', help='Export results to file')
    
    args = parser.parse_args()
    
    classifier = NumberClassifier(verbose=args.detailed)
    
    if args.numbers:
        # CLI mode
        for num in args.numbers:
            analysis = classifier.analyze_number(num)
            display_analysis(analysis, detailed=args.detailed)
        
        if args.batch and len(args.numbers) > 1:
            stats = classifier.analyze_batch(args.numbers)
            print(f"\nBatch Stats: Mean={stats.mean:.2f}, StdDev={stats.std_dev:.2f}")
        
        if args.visualize and len(args.numbers) > 1:
            print(classifier.visualize_distribution(args.numbers))
        
        if args.export:
            format_type = 'json' if args.export.endswith('.json') else 'csv'
            classifier.export_analysis(args.export, format_type)
    else:
        # Interactive mode
        interactive_mode(classifier)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 Program interrupted.")
    except Exception as e:
        print(f"❌ Error: {e}")
        sys.exit(1)
