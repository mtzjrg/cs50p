# camelCase: Implement a program that prompts the user for the name of a
#            variable in camel case and outputs the corresponding name in
#            snake case. Assume that the user's input will indeed be in
#            camel case

txt = input("camelCase: ")

print("snake_case: ", end="")
for c in txt:
    if c.isupper():
        print(f"_{c.lower()}", end="")
    else:
        print(c, end="")
print()
