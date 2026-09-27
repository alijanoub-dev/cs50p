import emoji

def main():
    emoji_str = input("Input: ")
    print(f"Output: {emoji.emojize(emoji_str)}")

if __name__ == "__main__":
    main()