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