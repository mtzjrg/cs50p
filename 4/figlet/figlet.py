# Frank, Ian and Glen's Letters: Implement a program that:
#
#       - Expects zero or two command-line arguments:
#           - Zero if the user would like to output text in a random font.
#           - Two if the user would like to output text in a specific font, in
#             which case the first of the two should be `-f` or `--font`, and
#             the second of the two should be the name of the font.
#       - Prompts the user for a `str` of text.
#       - Outputs that text in the desired font.
#
#       If the user provides two command-line arguments and the first is not
#       `-f` or `--font` or the second is not the name of a font, the program
#       should exit via sys.exit with and error message.

import random
import sys

from pyfiglet import Figlet

figlet = Figlet()
FONTS = figlet.getFonts()

match len(sys.argv):
    case 1:
        string = input("Input: ").strip()
        figlet.setFont(font=random.choice(FONTS))
        print(f"Output: \n{figlet.renderText(string)}")
    case 3:
        if sys.argv[1] in ["-f", "--font"] and sys.argv[2] in FONTS:
            string = input("Input: ").strip()
            figlet.setFont(font=sys.argv[2])
            print(f"Output: \n{figlet.renderText(string)}")
        else:
            sys.exit("Invalid usage")
    case _:
        sys.exit("Invalid usage")
