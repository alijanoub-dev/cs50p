def main():
    while True:
        try:
            fraction_str = input("Fraction: ")
            percentage = convert(fraction_str)
            print(gauge(percentage))
            break
        except (ValueError, ZeroDivisionError):
            pass

def convert(fraction):
    parts = fraction.split("/")
    if len(parts) != 2:
        raise ValueError
        
    x = int(parts[0])
    y = int(parts[1])
    
    if y == 0:
        raise ZeroDivisionError
    
    if x > y:
        raise ValueError
        
    return round((x / y) * 100)

def gauge(percentage):
    if percentage >= 99:
        return "F"
    elif percentage <= 1:
        return "E"
    else:
        return f"{percentage}%"

if __name__ == "__main__":
    main()