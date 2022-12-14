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

    #
    # YOUR CODE FOR TOPICS & RESPONSES HERE
    #

    "": [
        "Hey! Are you there?",
        "You know you can't just sit there silently like that!",
        ""
    ],

    "default" : [
        "I'm not sure what that means.",
        # ADD TWO MORE RESPONES
    ]

}

"""
STEP 3
Create related() function to find related text
Use temp_text for unedited user response and final_text for modified user_response
"""

def related(temp_text):
    if "name" in temp_text:
        final_text = "what's your name?"
    elif "robot" in temp_text:
        final_text = "are you a bot?"

    #
    # YOUR CODE HERE
    #

    else:
        final_text = temp_text
    return final_text

