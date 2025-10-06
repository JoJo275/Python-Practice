import csv
import os
import sys
from pathlib import Path

import pytest

# Import the module under test
sys.path.append(str(Path(__file__).resolve().parents[1]))
from format_text import format_text as ft


def test_format_paragraphs_basic():
    s = "First paragraph.\n\n  Second paragraph.\n\n\nThird."
    out = ft.format_paragraphs(s)
    assert out == "First paragraph.\n\nSecond paragraph.\n\nThird."


def test_format_paragraphs_nonstring():
    assert ft.format_paragraphs(None) == ''
    assert ft.format_paragraphs(123) == '123'


@pytest.mark.skipif(ft.pd is None, reason="pandas not installed")
def test_process_csv_roundtrip(tmp_path: Path):
    # Create input CSV
    in_file = tmp_path / "input.csv"
    out_file = tmp_path / "out.csv"

    rows = [
        {"id": 1, "text": "Para A.\n\nPara B."},
        {"id": 2, "text": "Only one paragraph."},
        {"id": 3, "text": None},
    ]

    # Write using pandas for fidelity
    import pandas as pd
    df = pd.DataFrame(rows)
    df.to_csv(in_file, index=False)

    # Run the processor
    ft.process_csv(str(in_file), str(out_file), column='text')

    # Read output and verify formatting
    out_df = pd.read_csv(out_file)
    assert out_df.loc[0, 'text'] == 'Para A.\n\nPara B.'
    assert out_df.loc[1, 'text'] == 'Only one paragraph.'
    assert out_df.loc[2, 'text'] == ''


def test_process_csv_without_column(tmp_path: Path):
    # Use a CSV that lacks the 'text' column; expect SystemExit
    in_file = tmp_path / "noc.txt.csv"
    out_file = tmp_path / "out.csv"

    # Write a minimal CSV (no text column)
    with open(in_file, 'w', newline='', encoding='utf-8') as f:
        w = csv.writer(f)
        w.writerow(['id', 'name'])
        w.writerow([1, 'Alice'])

    with pytest.raises(SystemExit):
        ft.process_csv(str(in_file), str(out_file), column='text')
