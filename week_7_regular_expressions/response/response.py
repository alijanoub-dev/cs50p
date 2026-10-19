from validator_collection import checkers


def main():
    email = input("What's your email address? ")
    if valid_email(email):
        print("Valid")
    else:
        print("Invalid")


def valid_email(e):
    return checkers.is_email(e)


if __name__ == "__main__":
    main()