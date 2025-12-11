# Fuel Gauge: Implement a program that prompts the user for a fraction,
#             as `X/Y`, wherein each of `X` and `Y` is a positive integer, and
#             then outputs, as a percentage rounded to the nearest integer, how
#             much fuel is in the tank. If, though, 1% or less remains, output
#             `E` instead to indicate that the tank is essentially empty. And if
#             99% or more remains, output `F` instead to indicate that the tank
#             essentially full.
#
#             If, though, `X` or `Y` is not an integer, `X` is greater than `Y`,
#             or `Y`is `0`, instead prompt the user again.

def main():
    fuel = get_fuel()

    if fuel >= 99:
        print("F")
    elif fuel <= 1:
        print("E")
    else:
        print(f"{fuel}%")


def get_fuel():
    while True:
        fraction = input("Fraction: ")
        try:
            x, y = fraction.split('/')
            if 0 <= (int(x) / int(y)) <= 1:
                return round((int(x) / int(y)) * 100)
        except (ValueError, ZeroDivisionError):
            pass


main()
