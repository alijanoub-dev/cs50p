import pyfiglet
import sys
import random

def main():
    figlet = pyfiglet.Figlet()
    avaiable_fonts = figlet.getFonts()

    if len(sys.argv) == 1:
        selected_font = random.choice(avaiable_fonts)

    elif len(sys.argv) == 3 and (sys.argv[1] == "-f" or sys.argv[1] == "--font"):
        selected_font = sys.argv[2]
        if selected_font not in avaiable_fonts:
            sys.exit("Invalid usage")

    else:
        sys.exit("Invalid usage")

    figlet.setFont(font=selected_font)

    user_input = input("Input: ")

    print("Output:")
    print(figlet.renderText(user_input))

if __name__ == "__main__":
    main()