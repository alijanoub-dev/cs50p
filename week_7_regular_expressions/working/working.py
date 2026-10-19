import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    pattern = fr"^([1-9]|1[0-2])(:[0-5][0-9])? (AM|PM) to ([1-9]|1[0-2])(:[0-5][0-9])? (AM|PM)$"

    match = re.search(pattern, s)
    if not match:
        raise ValueError("Invalid format")

    start_hour = int(match.group(1))
    start_minute = int(match.group(2)[1:]) if match.group(2) else 0
    start_ampm = match.group(3)

    end_hour = int(match.group(4))
    end_minute = int(match.group(5)[1:]) if match.group(5) else 0
    end_ampm = match.group(6)

    if start_ampm == "AM":
        if start_hour == 12:
            start_hour = 0
    else:
        if start_hour != 12:
            start_hour += 12

    if end_ampm == "AM":
        if end_hour == 12:
            end_hour = 0
    else:
        if end_hour != 12:
            end_hour += 12

    return f"{start_hour:02}:{start_minute:02} to {end_hour:02}:{end_minute:02}"


if __name__ == "__main__":
    main()