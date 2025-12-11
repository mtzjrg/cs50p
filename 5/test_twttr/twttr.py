# Testing my twttr: Reimplement twttr.py from Problem Set 2, restructuring the
#       the code to use a function to achieve the same result as before.

def main():
    print(f"Output: {shorten(input("Input: ").strip())}")


def shorten(word):
    VOWELS = [
        'a', 'e', 'i', 'o', 'u',
        'A', 'E', 'I', 'O', 'U'
    ]

    for c in word:
        if c in VOWELS:
            word = word.replace(c, "")
    return word


if __name__ == "__main__":
    main()
