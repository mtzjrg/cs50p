# Re-requesting a Vanity Plate: Reimplement plates.py from Problem Set 2,
#       restructuring your code to only call main if the value of `__name__` is
#       `"__main__"`

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


if __name__ == "__main__":
    main()
