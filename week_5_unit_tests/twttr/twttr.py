def main():
    user_input = input("Input: ").strip()
    new_user_input = ""
    
    print(f"Output: {shorten(user_input)}")

def shorten(word="Twitter"):
    new_user_input = ""

    for letter in word:
            if letter.lower() not in ["a", "e", "i", "o", "u"]:
                new_user_input += letter

    return new_user_input

if __name__ == "__main__":
    main()