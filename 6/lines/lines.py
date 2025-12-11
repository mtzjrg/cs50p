# Lines of Code: Implement a program that expects exactly one command-line
#       argument, the name (or path) of a Python file, and outputs the number
#       of lines of code in that file, excluding comments and blank lines. If
#       the user does not specify exactly one command-line argument, or if the
#       specified file's name does not end in `.py`, or if the specified file
#       does not exist, the program should instead exit via `sys.exit`.
#
#       Assume that any line that starts with `#`, optionally preceded by
#       whitespace, is a comment. (A docstring is not considered a comment.)
#       Assume that any line that only contains whitespace is blank.

import sys

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
if len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
if not sys.argv[1].endswith(".py"):
    sys.exit("Not a Python file")

line_count = 0
try:
    with open(sys.argv[1]) as file:
        for row in file:
            if not row.isspace() and not row.lstrip().startswith("# "):
                line_count += 1
except FileNotFoundError:
    sys.exit("File does not exist")
else:
    print(line_count)
