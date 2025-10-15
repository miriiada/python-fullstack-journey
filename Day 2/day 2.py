import random

# Task 1
# for i in range (1, 101):
#     if i % 3 == 0 and i % 5 == 0:
#         print("Fizz")
#     elif i % 3 == 0:
#         print("Buzz")
#     elif i % 5 == 0:
#         print("FizzBuzz")
#     else:
#         print(i)

# Task 2
secret = random.randint(1, 100)
attempts = 0

while True:
    attempts += 1
    print("Attept number:", attempts)
    try:
        num = int(input("Enter a number: "))
    except ValueError:
        print("Enter a number without symbols or letters")
        continue
    if num == secret:
        print("You've found the secret number! Congratulations! You've guessed the number in", attempts, "attempts!")
        break
    elif num < secret:
        if secret - num <= 15:
            print("Low")
        else:
            print("Too low")
    else:
        if num - secret <= 15:
            print("High")
        else:
            print("Too high")




    # else:
    #     print("Enter a number without symbols or letters")


