#!/usr/bin/env python3
"""password_checker.py

Advanced password strength checker with detailed analysis and recommendations.

Features:
    - Detailed strength scoring (0-100)
    - Multiple strength levels (Very Weak to Very Strong)
    - Visual strength meter
    - Specific feedback on improvements
    - Common password detection
    - Character variety analysis
    - Entropy calculation
"""

import re
import math
import string
from typing import Dict, List, Tuple, Optional
from dataclasses import dataclass
from enum import Enum
import getpass


class StrengthLevel(Enum):
    """Password strength levels."""
    VERY_WEAK = "Very Weak"
    WEAK = "Weak"
    MODERATE = "Moderate"
    STRONG = "Strong"
    VERY_STRONG = "Very Strong"


@dataclass
class PasswordAnalysis:
    """Detailed password analysis results."""
    password: str
    score: int
    strength_level: StrengthLevel
    length: int
    has_lowercase: bool
    has_uppercase: bool
    has_numbers: bool
    has_symbols: bool
    has_spaces: bool
    character_variety: int
    entropy: float
    is_common: bool
    suggestions: List[str]
    patterns_found: List[str]


class PasswordChecker:
    """Advanced password strength checker."""
    
    # Common weak passwords (top 100)
    COMMON_PASSWORDS = {
        'password', '123456', '12345678', 'qwerty', 'abc123', 'monkey', '1234567',
        'letmein', 'trustno1', 'dragon', 'baseball', 'iloveyou', 'master', 'sunshine',
        'ashley', 'bailey', 'passw0rd', 'shadow', '123123', '654321', 'superman',
        'password1', 'password123', 'welcome', 'admin', 'login', 'hello', '666666'
    }
    
    # Common patterns to detect
    KEYBOARD_PATTERNS = ['qwerty', 'asdf', 'zxcv', '1234', '4321', 'abcd', 'dcba']
    
    def __init__(self):
        """Initialize the password checker."""
        self.min_length = 8
        self.optimal_length = 12
        self.max_common_length = 14
    
    def check_strength(self, password: str) -> PasswordAnalysis:
        """
        Perform comprehensive password strength analysis.
        
        Args:
            password: The password to analyze
            
        Returns:
            PasswordAnalysis object with detailed results
        """
        # Basic checks
        length = len(password)
        has_lower = bool(re.search(r'[a-z]', password))
        has_upper = bool(re.search(r'[A-Z]', password))
        has_number = bool(re.search(r'\d', password))
        has_symbol = bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))
        has_space = ' ' in password
        
        # Calculate character variety
        char_types = sum([has_lower, has_upper, has_number, has_symbol, has_space])
        
        # Calculate entropy
        entropy = self._calculate_entropy(password)
        
        # Check if common password
        is_common = password.lower() in self.COMMON_PASSWORDS
        
        # Detect patterns
        patterns = self._detect_patterns(password)
        
        # Calculate score
        score = self._calculate_score(
            length, char_types, entropy, is_common, len(patterns)
        )
        
        # Determine strength level
        strength_level = self._get_strength_level(score)
        
        # Generate suggestions
        suggestions = self._generate_suggestions(
            length, has_lower, has_upper, has_number, has_symbol,
            is_common, patterns, char_types
        )
        
        return PasswordAnalysis(
            password=password,
            score=score,
            strength_level=strength_level,
            length=length,
            has_lowercase=has_lower,
            has_uppercase=has_upper,
            has_numbers=has_number,
            has_symbols=has_symbol,
            has_spaces=has_space,
            character_variety=char_types,
            entropy=entropy,
            is_common=is_common,
            suggestions=suggestions,
            patterns_found=patterns
        )
    
    def _calculate_entropy(self, password: str) -> float:
        """
        Calculate password entropy (bits of randomness).
        
        Args:
            password: The password to analyze
            
        Returns:
            Entropy value in bits
        """
        charset_size = 0
        
        if re.search(r'[a-z]', password):
            charset_size += 26
        if re.search(r'[A-Z]', password):
            charset_size += 26
        if re.search(r'\d', password):
            charset_size += 10
        if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
            charset_size += 32
        if ' ' in password:
            charset_size += 1
            
        if charset_size == 0:
            return 0
            
        entropy = len(password) * math.log2(charset_size)
        return round(entropy, 2)
    
    def _detect_patterns(self, password: str) -> List[str]:
        """
        Detect common patterns in password.
        
        Args:
            password: The password to analyze
            
        Returns:
            List of detected patterns
        """
        patterns = []
        password_lower = password.lower()
        
        # Check keyboard patterns
        for pattern in self.KEYBOARD_PATTERNS:
            if pattern in password_lower:
                patterns.append(f"Keyboard pattern: {pattern}")
        
        # Check repeated characters
        for i in range(len(password) - 2):
            if password[i] == password[i+1] == password[i+2]:
                patterns.append(f"Repeated character: {password[i]}")
                break
        
        # Check sequential numbers
        if re.search(r'(012|123|234|345|456|567|678|789)', password):
            patterns.append("Sequential numbers")
        
        # Check sequential letters
        if re.search(r'(abc|bcd|cde|def|efg|fgh|ghi|hij)', password_lower):
            patterns.append("Sequential letters")
        
        return patterns
    
    def _calculate_score(self, length: int, char_types: int, entropy: float,
                        is_common: bool, pattern_count: int) -> int:
        """
        Calculate overall password strength score (0-100).
        
        Args:
            length: Password length
            char_types: Number of character types used
            entropy: Password entropy
            is_common: Whether password is commonly used
            pattern_count: Number of patterns detected
            
        Returns:
            Score from 0 to 100
        """
        score = 0
        
        # Length scoring (0-30 points)
        if length >= 16:
            score += 30
        elif length >= 12:
            score += 25
        elif length >= 8:
            score += 15
        else:
            score += max(0, length * 2)
        
        # Character variety scoring (0-30 points)
        score += min(30, char_types * 7.5)
        
        # Entropy scoring (0-30 points)
        if entropy >= 60:
            score += 30
        elif entropy >= 40:
            score += 20
        elif entropy >= 25:
            score += 10
        else:
            score += max(0, entropy * 0.4)
        
        # Bonus points (0-10 points)
        if length >= 15 and char_types >= 4:
            score += 10
        elif length >= 12 and char_types >= 3:
            score += 5
        
        # Penalties
        if is_common:
            score = min(20, score)  # Cap at 20 if common password
        
        score -= pattern_count * 5  # Deduct for each pattern
        
        return max(0, min(100, int(score)))
    
    def _get_strength_level(self, score: int) -> StrengthLevel:
        """
        Convert score to strength level.
        
        Args:
            score: Password strength score (0-100)
            
        Returns:
            StrengthLevel enum value
        """
        if score >= 80:
            return StrengthLevel.VERY_STRONG
        elif score >= 60:
            return StrengthLevel.STRONG
        elif score >= 40:
            return StrengthLevel.MODERATE
        elif score >= 20:
            return StrengthLevel.WEAK
        else:
            return StrengthLevel.VERY_WEAK
    
    def _generate_suggestions(self, length: int, has_lower: bool, has_upper: bool,
                             has_number: bool, has_symbol: bool, is_common: bool,
                             patterns: List[str], char_types: int) -> List[str]:
        """
        Generate improvement suggestions.
        
        Returns:
            List of suggestion strings
        """
        suggestions = []
        
        if is_common:
            suggestions.append("⚠️ This is a commonly used password. Choose something unique!")
        
        if length < self.min_length:
            suggestions.append(f"📏 Increase length to at least {self.min_length} characters")
        elif length < self.optimal_length:
            suggestions.append(f"📏 Consider increasing length to {self.optimal_length}+ characters")
        
        if not has_lower:
            suggestions.append("🔡 Add lowercase letters (a-z)")
        if not has_upper:
            suggestions.append("🔠 Add uppercase letters (A-Z)")
        if not has_number:
            suggestions.append("🔢 Add numbers (0-9)")
        if not has_symbol:
            suggestions.append("🔣 Add special symbols (!@#$%^&*)")
        
        if patterns:
            suggestions.append("🔄 Avoid predictable patterns and sequences")
        
        if char_types < 3:
            suggestions.append("🎨 Use more character variety for better security")
        
        if length > 20 and char_types >= 4 and not patterns and not is_common:
            suggestions.append("✨ Excellent password strength!")
        
        return suggestions if suggestions else ["✅ Password meets all requirements"]


def is_strong_password(password: str) -> bool:
    """
    Check if the provided password is strong.
    
    Backward compatible function with original implementation.

    Args:
        password: The password string to check.
    Returns:
        True if the password is strong, False otherwise.
    Examples:
        >>> is_strong_password("Password1!")
        True
        >>> is_strong_password("weakpass")
        False
    """
    if len(password) < 8:
        return False

    has_upper = any(c.isupper() for c in password)
    has_number = any(c.isdigit() for c in password)
    has_symbol = any(not c.isalnum() for c in password)

    return has_upper and has_number and has_symbol


def display_analysis(analysis: PasswordAnalysis, show_password: bool = False) -> None:
    """
    Display password analysis results with visual indicators.
    
    Args:
        analysis: PasswordAnalysis object
        show_password: Whether to show the actual password
    """
    # Visual strength meter
    meter_length = 20
    filled = int((analysis.score / 100) * meter_length)
    meter = "█" * filled + "░" * (meter_length - filled)
    
    # Color codes (using ASCII)
    colors = {
        StrengthLevel.VERY_WEAK: "🔴",
        StrengthLevel.WEAK: "🟠",
        StrengthLevel.MODERATE: "🟡",
        StrengthLevel.STRONG: "🟢",
        StrengthLevel.VERY_STRONG: "🟢"
    }
    
    print("\n" + "="*50)
    print("PASSWORD STRENGTH ANALYSIS")
    print("="*50)
    
    if show_password:
        masked = analysis.password[:2] + "*" * (len(analysis.password) - 4) + analysis.password[-2:]
        print(f"Password: {masked}")
    
    print(f"Length: {analysis.length} characters")
    print(f"\n{colors[analysis.strength_level]} Strength: {analysis.strength_level.value}")
    print(f"Score: {analysis.score}/100 [{meter}]")
    print(f"Entropy: {analysis.entropy} bits")
    
    print("\n📋 Character Types:")
    print(f"  {'✅' if analysis.has_lowercase else '❌'} Lowercase letters")
    print(f"  {'✅' if analysis.has_uppercase else '❌'} Uppercase letters")
    print(f"  {'✅' if analysis.has_numbers else '❌'} Numbers")
    print(f"  {'✅' if analysis.has_symbols else '❌'} Special symbols")
    
    if analysis.patterns_found:
        print("\n⚠️ Patterns Detected:")
        for pattern in analysis.patterns_found:
            print(f"  • {pattern}")
    
    if analysis.suggestions:
        print("\n💡 Suggestions for Improvement:")
        for suggestion in analysis.suggestions:
            print(f"  • {suggestion}")
    
    print("="*50)


def interactive_mode():
    """Run interactive password checking mode."""
    checker = PasswordChecker()
    
    print("\n" + "="*50)
    print("INTERACTIVE PASSWORD STRENGTH CHECKER")
    print("="*50)
    
    while True:
        print("\n1. Check password strength")
        print("2. Test sample passwords")
        print("3. View password tips")
        print("4. Quit")
        
        choice = input("\nSelect option (1-4): ").strip()
        
        if choice == '1':
            password = getpass.getpass("\nEnter password to check (hidden): ")
            analysis = checker.check_strength(password)
            display_analysis(analysis, show_password=True)
            
        elif choice == '2':
            test_passwords = [
                "password",
                "Password1!",
                "weakpass",
                "Short1!",
                "MyP@ssw0rd123",
                "CorrectHorseBatteryStaple",
                "Tr0ub4dor&3",
                "qwerty123"
            ]
            
            print("\n" + "="*50)
            print("SAMPLE PASSWORD TESTS")
            print("="*50)
            
            for pwd in test_passwords:
                analysis = checker.check_strength(pwd)
                meter_length = 10
                filled = int((analysis.score / 100) * meter_length)
                meter = "█" * filled + "░" * (meter_length - filled)
                print(f"{pwd.ljust(25)} [{meter}] {analysis.score:3d}/100 - {analysis.strength_level.value}")
            
        elif choice == '3':
            print("\n" + "="*50)
            print("PASSWORD SECURITY TIPS")
            print("="*50)
            print("\n🔐 Best Practices:")
            print("  • Use at least 12 characters (16+ is better)")
            print("  • Mix uppercase, lowercase, numbers, and symbols")
            print("  • Avoid dictionary words and common patterns")
            print("  • Use passphrases: combine random words")
            print("  • Never reuse passwords across sites")
            print("  • Consider using a password manager")
            print("\n❌ What to Avoid:")
            print("  • Personal information (names, birthdays)")
            print("  • Keyboard patterns (qwerty, 123456)")
            print("  • Common substitutions (@ for a, 0 for o)")
            print("  • Single dictionary words")
            print("  • Previous passwords with minor changes")
            
        elif choice == '4':
            print("Goodbye!")
            break
        
        else:
            print("Invalid choice. Please select 1-4.")


def main():
    """Main function to run the password checker."""
    import sys
    
    if len(sys.argv) > 1:
        # Command line mode
        if sys.argv[1] == '--interactive' or sys.argv[1] == '-i':
            interactive_mode()
        else:
            # Check password provided as argument
            password = sys.argv[1]
            checker = PasswordChecker()
            analysis = checker.check_strength(password)
            display_analysis(analysis, show_password=False)
    else:
        # Default: run original test suite plus new interactive mode
        print("="*50)
        print("ORIGINAL COMPATIBILITY TEST")
        print("="*50)
        
        test_passwords = [
            "Password1!",
            "weakpass",
            "Short1!",
            "NoNumber!",
            "nouppercase1!",
            "NoSymbol1",
            "StrongPass123$"
        ]

        for pwd in test_passwords:
            result = is_strong_password(pwd)
            print(f"Password: {pwd.ljust(15)} Strong: {result}")
        
        print("\nRun with --interactive or -i for interactive mode")
        print("Or pass a password as argument to check it")


if __name__ == "__main__":
    main()
