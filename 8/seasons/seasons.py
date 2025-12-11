# Seasons of Love: Implement a program that prompts the user for their date of
#       birth in `YYYY-MM-DD` format and then prints how old they are in minutes
#       , rounded to the nearest integer, using English words instead of
#       numerals, just like the song from Rent, without any `and` between words.
#       Since a user might not know the time at which they were born, assume,
#       for simplicity, that the user was born at midnight (i.e., 00:00:00) on
#       that date. And assume that the current time is also midnight. In other
#       words, even if the user runs the program at noon, assume that it's
#       actually midnight, on the same date. Use `datetime.date.today` to get
#       today's date, per
#       https://docs.python.org/3/library/datetime.html#datetime.date.today

import sys
from datetime import date

import inflect
p = inflect.engine()


def main():
    bday = input("Date of Birth: ")

    if bday.upper().isupper():
        sys.exit("Invalid date")
    print(convert(bday))


def convert(bday):
    mins = date.today() - date.fromisoformat(bday)
    mins = p.number_to_words(mins.days * 24 * 60, andword='')
    return f"{mins.capitalize()} minutes"


if __name__ == "__main__":
    main()
