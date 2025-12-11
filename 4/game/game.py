# Guessing Game: Implement a program that:
#       - Prompts the user for a level, n. If the user does not input a positive
#         integer, the program should prompt the user again.
#       - Randomly generates an integer between 1 and n, inclusive, using the
#         random module
#       - Prompts the user to guess that integer. If the guess is not a positive
#         integer, the program should prompt the user again
#           - If the guess is smaller than that integer, the program should
#             output `Too small!` and prompt the user again
#           - If the guess it larger than that integer, the program should
#             output `Too large!` and prompt the user again
#           - If the guess is the same as that integer, the program should
#             output `Just right!` and exit


import random

while True:
    try:
        lvl = int(input("Level: ").strip())
    except ValueError:
        pass
    else:
        if lvl > 0:
            answer = random.randint(1, lvl)
            break

while True:
    try:
        guess = int(input("Guess: ").strip())
    except ValueError:
        pass
    else:
        if guess > 0:
            if guess < answer:
                print("Too small!")
            elif guess > answer:
                print("Too big!")
            else:
                print("Just right!")
                break
