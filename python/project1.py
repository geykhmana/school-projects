import random

def playgame():
    randomNumber = random.randint(1, 50)
    numberOfGuesses = 1
    playAgain = 1
    print("Guess a number between 1 and 50")
    i = 1
    while(numberOfGuesses < 11):
        guess = int(input("Enter the number that you think is correct: "))
        if (guess == randomNumber):
            print("Congratulations, you guessed the correct number randomNumber in", numberOfGuesses, "guesses!\n")
            break
        elif(guess < randomNumber):
            print("Your guess of", guess, "was too low")
        elif (guess > randomNumber):
            print("Your guess of", guess, "was too high")
        numberOfGuesses += 1;
        if (numberOfGuesses == GUESSES):
            print("You did not guess the right number. The correct number was", randomNumber)