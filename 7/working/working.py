# Working 9 to 5: Implement a function called `convert` that expects a `str` in
#       any of the 12-hour formats below and returns the corresponding `str` in
#       24-hour format (i.e., `9:00 to 17:00`). Expect that `AM` and `PM` will
#       be capitalized (with no periods therein) and that there will be a space
#       before each. Assume that these times are representative of actual times,
#       not necessarily 9:00 AM and 5:00 PM specifically
#
#       - 9:00 AM to 5:00 PM
#       - 9 AM to 5 PM
#       - 9:00 AM to 5 PM
#       - 9 AM to 5:00 PM
#
#       Raise a `ValueError` instead if the input to `convert` is not in either
#       of those formats or if either time is invalid (e.g., `12:60 AM`, `13:00
#       PM`, etc). But do not assume that someone's hours will start ante
#       meridiem and end post meridiem; someone might work late and even long
#       hours (e.g., `5:00 PM to 9:00 AM`).

import re


def main():
    print(convert(input("Hours: ")))


def convert(s):
    if matches := re.search(r"^(\d{1,2}):?(\d{2})? (AM|PM) to (\d{1,2}):?(\d{2})? (AM|PM)$", s):
        first_hour, first_min, first_meridiem, second_hour, second_min, second_meridiem = matches.groups()
    else:
        raise ValueError

    try:
        first_min = convert_min(first_min)
        second_min = convert_min(second_min)
    except ValueError:
        raise ValueError

    if first_hour.startswith('0') or second_hour.startswith('0'):
        raise ValueError
    if int(first_hour) > 12 or int(second_hour) > 12:
        raise ValueError

    first_hour = convert_hour(int(first_hour), first_meridiem)
    second_hour = convert_hour(int(second_hour), second_meridiem)

    return f"{first_hour:02}:{first_min:02} to {second_hour:02}:{second_min:02}"


def convert_min(min):
    if min:
        if int(min) > 59:
            raise ValueError
        else:
            return int(min)

    return 0


def convert_hour(hour, meridiem):
    match meridiem:
        case "AM":
            if hour == 12:
                hour = 0
        case "PM":
            if hour != 12:
                hour += 12

    return hour


if __name__ == "__main__":
    main()
