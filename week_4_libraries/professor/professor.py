import random

def main():
    level = get_level()
    score = 0

    for _ in range(10):
        i = 0
        x = generate_integer(level)
        y = generate_integer(level)
        z = x + y

        while i < 3:
            user_answer = int(input(f"{x} + {y} = "))
            i += 1
            if user_answer != z:
                print("EEE")
                continue
            else:
                break

        if user_answer == z:
            score += 1
        else:
            print(f"{x} + {y} = {z}")

    print(f"Score: {score}")

def get_level():
    while True:
        n = int(input("Level: "))

        if n in [1, 2, 3]:
            return n

def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    else:
        return random.randint(100, 999)

if __name__ == "__main__":
    main()