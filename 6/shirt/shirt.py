# CS50 P-Shirt: Implement a program that expects exactly two command-line
#       arguments:
#
#       - In `sys.argv[1]`, the name (or path) of a JPEG or PNG to read (i.e.,
#         open) as input
#       - In `sys.argv[2]`, the name (or path) of a JPEG or PNG to write (i.e.,
#         save) as output
#
#       The program should then overlay shirt.png (which has a transparent
#       background) on the input after resizing and cropping the input to be the
#       same size, saving the result as its output.
#
#       Assume the input will be a photo of someone posing in just the right way
#       , like in these demos (muppets.zip), so that, when they're resized and
#       cropped, the shirt appears to fit perfectly.
#
# shirt.png: https://cs50.harvard.edu/python/2022/psets/6/shirt/shirt.png
# muppets.zip: https://cs50.harvard.edu/python/2022/psets/6/shirt/muppets.zip

import os
import sys

from PIL import Image, ImageOps


if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
if len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

valid_extensions = [".jpg", ".jpeg", ".png"]
first_ext = os.path.splitext(sys.argv[1])[1]
second_ext = os.path.splitext(sys.argv[2])[1]

if first_ext not in valid_extensions:
    sys.exit("Invalid input")
if second_ext not in valid_extensions:
    sys.exit("Invalid output")
if first_ext != second_ext:
    sys.exit("Input and output have different extensions")

try:
    image = Image.open(sys.argv[1])
except FileNotFoundError:
    sys.exit("Input does not exist")

shirt = Image.open("shirt.png")
new_image = ImageOps.fit(image=image, size=shirt.size)
new_image.paste(shirt, shirt)
new_image.save(sys.argv[2])
