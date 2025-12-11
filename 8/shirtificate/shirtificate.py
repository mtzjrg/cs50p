# CS50 Shirtificate: Implement a program that prompts the user for their name
#       and outputs, using fpdf2, a CS50 shirtificate in a file called
#       `shirtificate.pdf` with these specifications:
#
#       - The orientation of the PDF should be Portrait.
#       - The format of the PDF should be A4, which is 210mm wide by 297mm tall.
#       - The top of the PDF should say "CS50 Shirtificate" as text, centered
#         horizontally.
#       - The shirt's image should be centered horizontally.
#       - The user's name should be on top of the shirt, in white text.

from fpdf import FPDF

pdf = FPDF(orientation='P', format="A4")
pdf.add_page()
pdf.set_font("helvetica", size=50)
pdf.set_font_size(24)
pdf.cell(w=None, h=55, text="CS50 Shirtificate", center=True, new_y="TOP")
pdf.image("shirtificate.png", x=10, y=70, w=190, h=190, keep_aspect_ratio=True)

with pdf.local_context(text_color=(255, 255, 255)):
    pdf.cell(w=None, h=260, text=f"{input("Name: ").strip()}", center=True)
pdf.output("shirtificate.pdf")
