import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    pattern = fr"\bum\b"
    match = re.findall(pattern, s, flags=re.IGNORECASE)

    return len(match)


if __name__ == "__main__":
    main()