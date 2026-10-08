import sys
import os
from PIL import Image
from PIL import ImageOps

def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")

    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    input_ext = os.path.splitext(sys.argv[1])[1].lower()
    output_ext = os.path.splitext(sys.argv[2])[1].lower()

    if input_ext not in [".jpg", ".jpeg", ".png"]:
        sys.exit("Invalid input")

    if input_ext != output_ext:
        sys.exit("Input and output have different extensions")

    try:
        user_image = Image.open(sys.argv[1])

    except FileNotFoundError:
        sys.exit("Input does not exist")

    shirt_image = Image.open("shirt.png")

    size = shirt_image.size

    user_image = ImageOps.fit(user_image, size)

    user_image.paste(shirt_image, shirt_image)

    user_image.save(sys.argv[2])

if __name__ == "__main__":
    main()