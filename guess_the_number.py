"""A simple number guessing game."""

import random

lucky_number = random.randint(1, 100)
print("Guess the lucky number between 1 and 100!")

while True:
    try:
        user_num = int(input("Guess the lucky number: "))
    except ValueError:
        print("Please enter a valid whole number.")
        continue

    if not 1 <= user_num <= 100:
        print("Please enter a number between 1 and 100.")
        continue

    if lucky_number == user_num:
        print("Correct guess! You won the game!")
        break
    elif user_num > lucky_number:
        print("Too high, try again.")
    else:
        print("Too low, try again.")

print("------ End the game ------")
