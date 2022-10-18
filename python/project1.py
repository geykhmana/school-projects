import random

def playgame():
    num = random.randint(1, 50)
    print("Guess a number between 1 and 50")
    i = 1
    guess1 = int(input(""))
    if guess1 == num:
        print("Correct! You guessed the number in", i, "attempts. Great job!")

