import sys
import csv

def main():
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")

    if not sys.argv[1].endswith(".csv"):
        sys.exit(f"Could not read {sys.argv[1]}")

    clean_list = []

    try:
        with open(sys.argv[1]) as file:
            reader = csv.DictReader(file)

            for row in reader:
                last_first = row["name"]
                last, first = last_first.split(",")

                row = {
                        "first": first.strip(),
                        "last": last.strip(),
                        "house": row["house"].strip()
                    }

                clean_list.append(row)

        with open(sys.argv[2], "w") as outfile:
            writer = csv.DictWriter(outfile, fieldnames=["first", "last", "house"])

            writer.writeheader()

            writer.writerows(clean_list)
            

    except FileNotFoundError:
            sys.exit("File does not exist")

if __name__ == "__main__":
    main()