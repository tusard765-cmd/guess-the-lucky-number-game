import random

luckynumber = random.randint(1, 100)

while True:
    user_num = int(input("Guess the lucky number: "))

    if luckynumber == user_num:
        print("Correct guess! You won the game!")
        break

    elif luckynumber < user_num:
        print("Too high, try again")

    elif luckynumber > user_num:
        print("Too low, try again")

print("------ End the game ------")