from fpdf import FPDF


def main():
  name = input("Name: ")

  pdf = FPDF(orientation="P", unit="mm", format="A4")
  pdf.add_page()

  pdf.set_font("helvetica", "B", 45)
  pdf.cell(0, 60, "CS50 Shirtificate", align="C")

  pdf.image("shirtificate.png", x=10, y=70, w=190)

  pdf.set_font("helvetica", "B", 30)
  pdf.set_text_color(255, 255, 255)
  pdf.text(x=55, y=145, txt=f"{name} took CS50")

  pdf.output("shirtificate.pdf")


if __name__ == "__main__":
  main()