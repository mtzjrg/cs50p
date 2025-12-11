# Pizza Py: Implement a program that expects exactly one command-line argument,
#       the name (or path) of a CSV file in Pinocchio's format, and outputs a
#       table formatted as ASCII art using `tabulate`, a package on PyPi at
#       https://pypi.org/project/tabulate/. Format the table using the library's
#       `grid` format. If the user does not specify exactly one command-line
#       argument, or if the specified file's name does not end in `.csv`, or if
#       the specified file's name does not exist, the program should instead
#       exit via `sys.exit`.

# regular.csv: https://cs50.harvard.edu/python/2022/psets/6/pizza/regular.csv
# sicilian.csv: https://cs50.harvard.edu/python/2022/psets/6/pizza/sicilian.csv

import csv
import sys

from tabulate import tabulate


if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
if len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
if not sys.argv[1].endswith(".csv"):
    sys.exit("Not a CSV file")

menu = []
try:
    with open(sys.argv[1]) as file:
        reader = csv.DictReader(file)
        for row in reader:
            menu.append(row)
except FileNotFoundError:
    sys.exit("File does not exist")
else:
    print(tabulate(menu, headers="keys", tablefmt="grid"))
