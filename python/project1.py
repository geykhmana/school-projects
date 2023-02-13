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
    randomNumber = random.randint(1, 50)    #Setting random number
    numberOfGuesses = 0                     #Setting number of guesses to 0 initially
    print("Guess a number between 1 and 50")
    while True:
        guess = int(input("\nEnter the number that you think is correct: "))
        numberOfGuesses += 1; #Right after input is gathered, guess count increases by 1
        if guess == randomNumber: #Correct guess case
            print("Congratulations, you guessed the correct number", randomNumber, "in", numberOfGuesses, "guesses!")
            response = playAgain() #Asks if user wants to play again
            if response == 1:
                numberOfGuesses = 0
                randomNumber = random.randint(1, 50) #Variables are reset, program automatically restarts due to while True loop
            elif response == 0:
                break #Loop breaks, program ends
        elif guess < randomNumber:
            print("Your guess of", guess, "was too low") #Guess is too low case
        elif guess > randomNumber:
            print("Your guess of", guess, "was too high") #Guess is too high case
        if numberOfGuesses == 10:
            print("You did not guess the right number. The correct number was", randomNumber)
            response = playAgain() #Asks if user wants to play again
            if response == 1:
                numberOfGuesses = 0
                randomNumber = random.randint(1, 50) #Variables are reset, program automatically restarts due to while True loop
            elif response == 0:
                break #Loop breaks, program ends

playGame()