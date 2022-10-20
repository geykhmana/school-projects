import random

def playAgain():
    while True:
        answer = input("\nWould you like to play again? Type Y for yes or N for no. ")
        if answer == "Y":
            return 1
            break
        elif answer == "N":
            print("Thanks for playing!")
            return 0
            break
        else:
            print("Error: Your response is invalid.")

def playGame():
    randomNumber = random.randint(1, 50)
    numberOfGuesses = 0
    print("Guess a number between 1 and 50")
    while numberOfGuesses < 11:
        guess = int(input("\nEnter the number that you think is correct: "))
        numberOfGuesses += 1;
        if guess == randomNumber:
            print("Congratulations, you guessed the correct number", randomNumber, "in", numberOfGuesses, "guesses!")
            response = playAgain()
            if response == 1:
                numberOfGuesses = 0
                randomNumber = random.randint(1, 50)
            elif response == 0:
                break
        elif guess < randomNumber:
            print("Your guess of", guess, "was too low")
        elif guess > randomNumber:
            print("Your guess of", guess, "was too high")
        if numberOfGuesses == 10:
            print("You did not guess the right number. The correct number was", randomNumber)
            response = playAgain()
            if response == 1:
                numberOfGuesses = 0
                randomNumber = random.randint(1, 50)
            elif response == 0:
                break

playGame()