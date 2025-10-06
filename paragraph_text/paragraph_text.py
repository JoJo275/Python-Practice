"""

In a file called paragraph_text.py, implement a program that:

Expects the user to provide two command-line arguments:
the name of an existing txt file to read as input, whose text is random or 
messy, and
the name of a new .txt to write as output.
Converts that input to that output, formatting the text so that paragraphs are
separated by a single blank line. Paragraphs are defined as blocks of text
separated by one or more blank lines. Leading and trailing whitespace should be
stripped from each paragraph. Sequences of multiple blank lines should be
replaced by a single blank line. Different speakers should be labaeled as
different paragraphs.

If the user does not provide exactly two command-line arguments, or if the
first cannot be read, or if the file is blank, or if the
specified file’s name does not end in .txt, or if the specified file does not
exist, the program should exit via sys.exit with an error
message.


"""

# !/usr/bin/env python3


input_path = "/mnt/data/[CLASSICAL MUSIC].txt"
output_path = "/mnt/data/[CLASSICAL MUSIC]_reformatted.txt"

with open(input_path, "r", encoding="utf-8") as f:
    text = f.read()

# Replace multiple newlines with a single blank line (two newlines total)
import re
clean_text = re.sub(r'\n\s*\n+', '\n\n', text.strip())

# Write the cleaned text to a new file
with open(output_path, "w", encoding="utf-8") as f:
    f.write(clean_text)

output_path

