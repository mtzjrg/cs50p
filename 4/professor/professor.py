# Little Profesor: Implement a program that:
#       - Prompts the user for a level, n. If the user does not input `1`, `2`,
#         or `3`, the program should prompt again.
#       - Randomly generates ten (10) math problems formatted as `X + Y = `,
#         wherein each of `X` and `Y` is a non-negative integer with n digits.
#         No need to support operations other than addition (`+`)
#       - Prompts the user to solve each of those problems. If an answer if not
#         correct (or not even a number), the program should output `EEE` and
#         prompt the user again, allowing the user up to three tries in total
#         for that problem. If the user has still not answered correctly after
#         three tries, the program should output the correct answer.
#       - The program should ultimately output the user's score: the number of
#         correct answers out of 10.

import random


def main():
    lvl = get_level()
    score = 0

    for _ in range(10):
        fails = 0
        x = generate_integer(lvl)
        y = generate_integer(lvl)
        solution = x + y

        while True:
            if fails == 3:
                print(f"{x} + {y} = {solution}")
                break

            try:
                answer = int(input(f"{x} + {y} = "))
                if answer != solution:
                    raise ValueError
            except ValueError:
                fails += 1
                print("EEE")
                pass
            else:
                score += 1
                break

    print(f"Score: {score}")


def get_level():
    while True:
        try:
            n = int(input("Level: ").strip())
        except ValueError:
            pass
        else:
            match n:
                case 1 | 2 | 3:
                    return n
                case _:
                    pass


def generate_integer(level):
    match level:
        case 1:
            return random.randint(0, 9)
        case 2:
            return random.randint(10, 99)
        case 3:
            return random.randint(100, 999)
        case _:
            raise ValueError


if __name__ == "__main__":
    main()
