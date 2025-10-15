# Project day 1: Calculator v1
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return None
    return a / b


def main():
    while True:
        first_number = int(input("Enter first number: "))
        second_number = int(input("Enter second number: "))
        action_number = input("What shall we do with the numbers? Enter one of the following symbols: +, -, *, /: ")

        if action_number == "+":
            result = add(first_number, second_number)
        elif action_number == "-":
            result = subtract(first_number, second_number)
        elif action_number == "*":
            result = multiply(first_number, second_number)
        elif action_number == "/":
            result = divide(first_number, second_number)
            if result is None:
                print("Error: Cannot divide by zero!")
        else:
            print("Unknown operation")
            continue

        print(f"Result: {result}")

        continue_calc = input("Continue? (y/n): ")
        if continue_calc.lower() != 'y':
            break
    print("Goodbye!")


if __name__ == "__main__":
    main()