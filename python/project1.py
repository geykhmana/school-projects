import random

def playAgain():
    answer = input("Would you like to play again? Type Y for yes or N for no.")
    if answer == "Y":
        return 1
    elif answer == "N":
        print("Thanks for playing!")
        return 0
    else:
        print("Error: your input was invalid.\n")
        playAgain()

def playGame():
    randomNumber = random.randint(1, 50)
    numberOfGuesses = 0
    print("Guess a number between 1 and 50")
    i = 1
    while(numberOfGuesses < 11):
        guess = int(input("Enter the number that you think is correct: "))
        if (guess == randomNumber):
            print("Congratulations, you guessed the correct number", randomNumber, "in", numberOfGuesses, "guesses!")
            numberOfGuesses = 0
            response = playAgain()
            if response == 0:
                break
        elif(guess < randomNumber):
            print("Your guess of", guess, "was too low")
        elif (guess > randomNumber):
            print("Your guess of", guess, "was too high")
        numberOfGuesses += 1;
        if (numberOfGuesses == 10):
            print("You did not guess the right number. The correct number was", randomNumber)
            numberOfGuesses = 0
            response = playAgain()
            if response == 0:
                break

playGame()