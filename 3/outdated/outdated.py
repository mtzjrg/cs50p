# Outdated: Implement a program that prompts the user for a date, anno Domini,
#       in month-day-year order, formatted like `9/8/1636` or `September 8, 1636`
#       , wherein the month in the latter might be any of the months of the year
#       Then output that same date in `YYYY-MM-DD` format. If the user's input
#       is not a valid date in either format, prompt the user again.
#
#       Assume that every month has no more than 31 days; no need to validate
#       whether a month has 28, 29, 30, or 31 days.


def main():
    while True:
        try:
            print(format_date(input("Date: ").strip()))
        except ValueError:
            pass
        else:
            break


def format_date(d):
    MONTHS = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
    ]

    if ' ' in d:
        month, day, year = d.split(' ')
        month = MONTHS.index(month) + 1
        day = int(day.removesuffix(','))

        if day < 1 or day > 31:
            raise ValueError
    else:
        month, day, year = d.split('/')
        month = int(month)
        day = int(day)

        if (day < 1 or day > 31) or (month < 1 or month > 12):
            raise ValueError
    year = int(year)

    return f"{year:04}-{month:02}-{day:02}"


main()
