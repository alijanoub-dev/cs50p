from datetime import date
import sys
import inflect

p = inflect.engine()


class User:
    def __init__(self, birth_date=""):
        try:
            self.date = date.fromisoformat(birth_date)
        except ValueError:
            sys.exit("Invalid date")

    def minutes_since_birth(self):
        today = date.today()
        difference = today - self.date
        minutes = difference.days * 24 * 60
        words = p.number_to_words(minutes, andword="")
        return words.capitalize()


def main():
    birth_date_str = input("Date of birth: ").strip()
    user = User(birth_date_str)
    print(f"{user.minutes_since_birth()} minutes")


if __name__ == "__main__":
    main()