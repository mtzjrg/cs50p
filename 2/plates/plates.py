# Vanity Plates: Implement a program that prompts the user for a vanity plate
#                and then output `Valid` if meets all of the requirements or
#                `Invalid` if it does not. Assume that any letters in the user's
#                input will be uppercase

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if 2 <= len(s) <= 6 and s.isalnum() and s[0:2].isalpha():
        for c in s:
            if c.isdigit():
                idx = s.index(c)
                if s[idx:].isdigit() and c != '0':
                    return True
                else:
                    return False
        return True
    else:
        return False


main()
