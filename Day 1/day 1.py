# 1 task
# user_name = input("Enter you name:")
# user_age = input("Enter you age:")
#
# print(f"Hello, {user_name}! You are {user_age} years old.")

# 2 task
# first_number = int(input("Enter first number:"))
# second_number = int(input("Enter second number:"))
#
# sum = first_number + second_number
# difference = first_number - second_number
# multiplication = first_number * second_number
# division = first_number / second_number
# remainder = first_number % second_number
#
# print(f"Sum: {sum}\n Difference: {difference}\n Multiplication: {multiplication}\n Division: {division}\n Remainder: {remainder}")
# Можно еще записать через def calculate_operations():

# 3 task
# user_text = input("Enter a text:")
# text_length = len(user_text)
# text_upper = user_text.upper()
# text_lower = user_text.lower()
# text_first_char = user_text[0]
# text_second_char = user_text[-1]
# text_reversed = user_text[::-1]
#
# print(f"String length: {text_length}\n Uppercase: {text_upper}\n Lowercase: {text_lower}\n First character: {text_first_char}\n Last character: {text_second_char}\n Reversed string: {text_reversed}")

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
    first_number = int(input("Enter first number: "))
    second_number = int(input("Enter second number: "))
    action_number = input("What shall we do with the numbers? Enter one of the following symbols: +, -, *, /: ")
    # action_number_int = int(action_number)
    # if action_number == "+":
    #     return add(first_number, second_number)
    # elif action_number == "-":
    #     return subtract(first_number, second_number)
    # elif action_number == "*":
    #     return multiply(first_number, second_number)
    # elif action_number == "/":
    #     return divide(first_number, second_number)
    # else:
    #     return "Unknown operation you need enter one the following symbols: +, -, *, /: "
    if action_number == "+":
        print(add(first_number, second_number))
    elif action_number == "-":
        print(subtract(first_number, second_number))
    elif action_number == "*":
        print(multiply(first_number, second_number))
    elif action_number == "/":
        print(divide(first_number, second_number))
    else:
        print("Unknown operation you need enter one the following symbols: +, -, *, /")


if __name__ == "__main__":
    main()






# print(34 * -1)
# # def opposite(number):
# #     if number >= 0:
# #         return number * -1
# #     if number <= 0:
# #         return number * 1
# #     else:
# #         return number
# # print(opposite)
#
# def string_to_number(s):
#     int(string_to_number)
# print(type(int("100")))