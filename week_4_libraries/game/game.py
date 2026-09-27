import random

def main():
    n = get_level()
    random_num = random.randint(1, n)
    
    while True:
        guess = get_guess()

        if random_num > guess:
            print("Too small!")
        elif random_num < guess:
            print("Too big!")
        else:
            print("Just right!")
            break

def get_guess():
    while True:
        try:
            guess = int(input("Guess: "))
        
        except ValueError:
            pass
        
        else:
            if guess > 0:
                return guess


def get_level():
    while True:
            try:
                n = int(input("Level: "))
    
            except ValueError:
                pass

            else:
                if n > 0:
                    return n

if __name__ == "__main__":
    main()