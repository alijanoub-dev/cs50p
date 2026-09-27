import inflect

def main():
    p = inflect.engine()
    names_list = []

    while True:
        try:
            name = input("Input: ")
            names_list.append(name)

        except EOFError:
            print()
            break

    clean_list = p.join(names_list)
    print(f"Adieu, adieu, to {clean_list}")

if __name__ == "__main__":
    main()