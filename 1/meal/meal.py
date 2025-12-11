# Meal Time: Implement a program that prompts the user for a time and outputs
#            whether it's `breakfast time`, `lunch time`, or `dinner time`. If
#            it's not time for a meal, don't output anything at all. Assume that
#            the user's input will be formatted in 24-hour time as #:## or ##:##.
#            Each meal's time range is inclusive (7:00 -> 8:00, breakfast time)
#
# Challenge: Optionally add support for 12-hour times: #(#):## a.m., #(#):## p.m.

def main():
    time = convert(input("What time is it? "))
    match time:
        case time if 7 <= time <= 8:
            print("breakfast time")
        case time if 12 <= time <= 13:
            print("lunch time")
        case time if 18 <= time <= 19:
            print("dinner time")


def convert(time):
    hours, minutes = time.split(":")

    match hours:
        case "12" if minutes.endswith("a.m."):
            hours = 0
        case hours if minutes.endswith("p.m.") and int(hours) != 12:
            hours = int(hours) + 12
        case _:
            hours = int(hours)
    minutes = int(minutes.rstrip("a.m.").rstrip("p.m.")) / 60

    return hours + minutes


if __name__ == "__main__":
    main()
