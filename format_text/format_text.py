"""A small CLI utility that formats paragraph text stored inside a CSV.

The program expects two positional arguments: an input CSV path and an
output CSV path. The input CSV is expected to contain a column named
"text" with paragraph-like values. Each cell's text will be normalized so
that paragraphs are trimmed and separated by a single blank line.

The formatter is intentionally conservative:
- it treats any sequence of one or more blank lines as a paragraph separator
- it strips leading/trailing whitespace from each paragraph

Errors are reported via sys.exit(...) with a clear message to make the tool
script-friendly.
"""

# !/usr/bin/env python3

from __future__ import annotations

import argparse
import os
import re
import sys
from typing import Callable

try:
    import pandas as pd
except Exception:  # Keep import error for runtime when user runs the CLI
    pd = None  # type: ignore[assignment]


_BLANK_LINES_RE = re.compile(r"\s*\n(?:\s*\n)+")


def format_paragraphs(text: str) -> str:
    """Normalize paragraph separation in a block of text.

    Rules:
    - Treat runs of one or more blank lines as paragraph separators.
    - Strip leading/trailing whitespace from each paragraph.
    - Ensure a single blank line between paragraphs in the output.

    Returns the formatted text. If `text` is empty or only whitespace, an
    empty string is returned.
    """
    if not isinstance(text, str):
        # Defensive: some CSVs may contain non-string types (NaN, numbers).
        return '' if text is None else str(text)

    # Split on runs of blank lines (one-or-more). Keep non-empty paragraphs.
    parts = [p.strip() for p in _BLANK_LINES_RE.split(text) if p.strip()]
    return "\n\n".join(parts)


def _validate_args(args: argparse.Namespace) -> None:
    """Validate parsed CLI args and exit with a helpful message on error."""
    input_csv = args.input

    if not input_csv.lower().endswith('.csv'):
        sys.exit("Error: input file must have a .csv extension")

    if not os.path.exists(input_csv):
        sys.exit(f"Error: input file does not exist: {input_csv}")

    # If pandas isn't installed, fail early with a helpful hint.
    if pd is None:
        sys.exit(
            "Error: pandas is required to run this script."
            " Install with 'pip install pandas'."
        )


def process_csv(input_csv: str, output_csv: str, column: str = 'text',
                formatter: Callable[[str], str] = format_paragraphs) -> None:
    """Read input CSV, format the given text column, and write the output CSV.

    Raises SystemExit on user-visible errors.
    """
    try:
        df = pd.read_csv(input_csv)
    except Exception as e:
        sys.exit(f"Error reading CSV '{input_csv}': {e}")

    if column not in df.columns:
        sys.exit(f"Error: CSV must contain a '{column}' column")

    # Apply formatter safely (handle NaN)
    df[column] = df[column].fillna('').apply(formatter)

    try:
        df.to_csv(output_csv, index=False)
    except Exception as e:
        sys.exit(f"Error writing CSV '{output_csv}': {e}")


def main() -> None:
    parser = argparse.ArgumentParser(
        description=(
            "Format paragraph text inside a CSV file"
        )
    )
    parser.add_argument(
        'input', help='Path to input CSV file'
    )
    parser.add_argument(
        'output', help='Path to output CSV file'
    )
    parser.add_argument(
        '--column', '-c',
        default='text',
        help="Name of the text column to format (default: 'text')",
    )
    args = parser.parse_args()

    _validate_args(args)
    process_csv(args.input, args.output, column=args.column)
    print(f"Formatted file written to: {args.output}")


if __name__ == '__main__':
    main()
