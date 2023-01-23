#
#   CSIT104-08 | Jesse Miller
#   Project 2 - ChatBot PART II
#
#   YOUR NAME HERE
#

import random


""" 
STEP 1
Print welcome message, get user_name, print personal hello
Enter your code below
"""

print("Hello, user whose name I currently do not know. I hope you are doing well at this moment.")


username = input("What is your name?")


print("It is a pleasure to meet you", username, " I would like to get to know you better.")

userresponse = input("Ask me a question: ")


# Variables for bot and user templates - edit with your bot's name!

bottemplate = "botboi3000: {0}"
usertemplate = username + ": {0}"


"""
STEP 2
Declare botname
Create a dictionary of chatbot responses
"""

# ENTER YOUR BOTNAME HERE
botname = "botboi3000"

# ADD YOUR RESPONSES TO THE DICTIONARY
responses = {

    "what's your name?" : [
        "I go by {0}".format(botname),
        "I am called {0}".format(botname),
        "My name is {0}".format(botname),
        "Many call me by the name of {0}".format(botname)
    ],

    "are you a bot?" : [
        "Oh no, you figured out my secret!",
        "Maybe - what do you think?",
        "Yes, I am just a bot."
    ],

    "what's your favorite color?" : [
        "My favorite color is green. I think it's calming.",
        "I like blue cuz it's chill and stuff.",
        "idk, you tell me i'm just a robot or whatever."
    ],

    "what do you do in your free time?" : [
        "I like to contemplate the significance of the existence of the universe.",
        "I chill and stuff.",
        "Oh I'm totally a Star Trek superfan and I constantly collect merch and make a references when I talk to anyone..."
    ],

    "do you like sauce?" : [
        "What the hell kinda question is that? Why would you put that on your Python Project? Are you really THAT out of ideas?",
        "Yeah it's good.",
        "Define sauce for me, please..."
    ],

    "": [
        "Hey! Are you there?",
        "You know you can't just sit there silently like that!",
        "Sorry, I can't speak mute."
    ],

    "stop": [
        "OK, goodbye",
        "Farewell, friend.",
        "Fine, then. Bye."
    ],

    "default" : [
        "I'm not sure what that means.",
        "OK, you might want to ask something else or spell better lol",
        "Sorry, I spaced out. What did you say again?"
    ]

}

"""
STEP 3
Create related() function to find related text
Use temptext for unedited user response and finaltext for modified userresponse
"""

def related(temptext):
    if "name" in temptext:
        finaltext = "what's your name?"
    elif "robot" in temptext or "bot" in temptext:
        finaltext = "are you a bot?"
    elif "color" in temptext:
        finaltext = "what's your favorite color?"
    elif "free time" in temptext or "freetime" in temptext:
        finaltext = "what do you do in your free time?"
    elif "sauce" in temptext:
        finaltext = "do you like sauce?"
    elif "stop" in temptext or "end" in temptext:
        finaltext = "stop"
    else:
        finaltext = "default"

    a = random.randint(0, 2)
    return responses[finaltext][a]

while True:
    thingtoprint = related(userresponse)
    print(thingtoprint)
    if thingtoprint == "OK, goodbye" or thingtoprint == "Farewell, friend." or thingtoprint == "Fine, then. Bye.":
        break
    userresponse = input()


#
#   PART II Starter
#


"""
STEP 1
Create respond function:
    - Takes one parameter (message)
    - Checks if message is in responses dictionary
    - If it is, set bot_message = a random resopnse
    - Otherwise, set bot_message to a random default message
    - return bot_message

THIS FUNCTION HAS BEEN CREATED FOR YOU!!
"""

def respond(message):
    if message in responses:
        bot_message = random.choice(responses[message])
    else:
        bot_message = random.choice(responses["default"])
    return bot_message


"""
STEP 2
Create send_message function:
   - Takes two parameters, message and temporary text (temp_text)
   - Prints the user's message formatted with the user_template
   - Calls the respond function on the temporary text and saves it to a variable named response
   - Prints the bot's reponse formatted with the bot_template   
"""

def send_message(message, temp_text):
    #
    #   YOUR CODE HERE
    #
    print("\n")

"""
STEP 3
Create the main loop to run the program:
    - Create a while loop that will run until a sentinel value (exit or stop) is entered (i.e., while(1) or while(True) - included below)
    - Prompt the user to enter a question or topic and save to variable named user_input
    - Use lower() function to normalize text to lowercase for comparison
    - Check if user_input is equal to "exit" or "stop"
    - If so, break out of loop (program ends)
    - Call related() function on user_input to get related topics (included below)
    - Call send_message function with user_input and related_text to have bot respond (included below)
"""
while 1:
    #
    #   YOUR CODE HERE
    #

    related_text = related(user_input)
    send_message(user_input, related_text)