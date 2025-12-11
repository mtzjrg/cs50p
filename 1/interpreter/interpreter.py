# Math Interpreter: Implement a program that prompts the user for an arithmetic
#           expression and then calculates and outputs the result as a floating
#           -point value formatted to one decimal place. Assume the input will
#           be formatted as `x y z`, with one space between `x` and `y` and one
#           space between `y` and `z` with `x` and `z` as integers and `y` as
#           operators
#
#           Assume that, if `y` is `/`, then `z` will not be `0`

def main():
    x, y, z = input("Expression: ").split(" ")
    print(calculate(int(x), int(z), y))

def calculate(n1, n2, op):
    match op:
        case "+":
            solution = n1 + n2
        case "-":
            solution = n1 - n2
        case "*":
            solution = n1 * n2
        case "/":
            solution = n1 / n2

    return float(solution)

main()
