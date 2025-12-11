# Back to the Bank: Reimplement bank.py from Problem Set 1, restructuring your
#       code to use a function to achieve the same result as before.

def main():
    print(value(input("Greeting: ")))


def value(greeting):
    greeting = greeting.strip().lower()
    if greeting.startswith("hello"):
        return 0
    elif greeting.startswith("h"):
        return 20

    return 100


if __name__ == "__main__":
    main()
