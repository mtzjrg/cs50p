# Scourgify: Implement a program that:
#       - Expects the user to provide two command-line arguments:
#           - the name of an existing CSV file to read as input, whose columns
#             are assumed to be, in order, `name` and `house`, and
#           - the name of a new CSV to write as output, whose columns should be,
#             in order, `first`, `last`, and `house`.
#       - Converts that input to that output, splitting each `name` into a
#         `first` name and `last` name. Assume that each student will have both
#         a first name and last name.
#
#       If the user does not provide exactly two command-line arguments, or if
#       the first cannot be read, the program should exit via `sys.exit` with
#       an error message.
#
# before.csv: https://cs50.harvard.edu/python/2022/psets/6/scourgify/before.csv

import csv
import sys


if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
if len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

students = []
try:
    with open(sys.argv[1]) as file:
        reader = csv.DictReader(file)
        for row in reader:
            last, first = row["name"].split(',')
            students.append({
                "first": first.strip(),
                "last": last.strip(),
                "house": row["house"]
            })
except FileNotFoundError:
    sys.exit(f"Could not read {sys.argv[1]}")
else:
    with open(sys.argv[2], 'w') as new_file:
        first_row = ["first", "last", "house"]
        writer = csv.DictWriter(new_file, fieldnames=first_row)
        writer.writeheader()
        for student in students:
            writer.writerow({
                "first": student["first"],
                "last": student["last"],
                "house": student["house"]
            })
