import sys
from tabulate import tabulate
import csv

def main():
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")

    if not sys.argv[1].endswith(".csv"):
        sys.exit("Not a CSV file")

    menue = []

    try:
        with open(sys.argv[1]) as file:
        
            reader = csv.DictReader(file)

            for row in reader:
                menue.append(row)

    except FileNotFoundError:
            sys.exit("File does not exist")

    print(tabulate(menue, headers="keys", tablefmt="grid"))

if __name__ == "__main__":
    main()