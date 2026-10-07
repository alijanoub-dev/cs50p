import sys

def main():
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")

    if not sys.argv[1].endswith(".py"):
        sys.exit("Not a Python file")

    counter = 0
    try:
        with open(sys.argv[1]) as file:
            for line in file:
                cleaned_line = line.strip()

                if cleaned_line != "" and not cleaned_line.startswith("#"):
                    counter += 1

    except FileNotFoundError:
        sys.exit("File does not exist")

    print(counter)

if __name__ == "__main__":
    main()