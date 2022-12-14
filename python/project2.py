#
#   CSIT104-08 | Jesse Miller
#   Project 2 - ChatBot PART I
#
#   Alan Geykhman
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

    "what's your favorite color?" : [
        "My favorite color is green. I think it's calming.",
        "I like blue cuz it's chill and stuff.",
        "idk, you tell me i'm just a robot or whatever."
    ],

    "": [
        "Hey! Are you there?",
        "You know you can't just sit there silently like that!",
        "Sorry, I can't speak mute."
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
    elif "robot" in temptext:
        finaltext = "are you a bot?"

    #
    # YOUR CODE HERE
    #

    else:
        finaltext = temptext
    return finaltext

