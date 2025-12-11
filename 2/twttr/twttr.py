# Just setting up my twttr: Implement a program that prompts for a `str` of
#           text and then outputs that same text but with all vowels omitted,
#           whether inputted in uppercase or lowercase. [A, E, I, O, U]

string = input("Input: ")

print("Output: ", end="")
for c in string:
    if c.lower() in ['a', 'e', 'i', 'o', 'u']:
        print("", end="")
    else:
        print(c, end="")
print()
