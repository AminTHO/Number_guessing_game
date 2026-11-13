import random

number = random.randint(1, 100)


while True:

    try:
        guess = int(input("Guess the number between 1 and 100 :"))
        if guess > 100:
            print("number out of range , please enter number between 1 and 100")

        elif number > guess:
            print("Too low")

        elif number < guess:
            print("Too high")

        else:
            print("Correct!")
            break
    except:
        print("please enter a valid number and try again")
