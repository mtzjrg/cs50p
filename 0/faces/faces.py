# Making Faces: Implement a function called `convert` that accepts a `str` as
#               input and returns the same input with any :) or :( to emoji.
#
#               Implement a function called main that prompts the user for
#               input, calls `convert` on that input and prints the result.

def main():
    print(convert(input("")))

def convert(s):
    return s.replace(":)", "🙂").replace(":(", "🙁")


main()
