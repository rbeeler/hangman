import random
"""
This is our Hangman Game!

It will be a simple command prompt game until we are ready 
to add more front-end fancifulness to it.

Please enjoy!
"""

#import methods
import time

#hello player
player = input("Please enter your Name: ")
time.sleep(1)
print ("Hello, " + player + "! Let's begin!")


# random word generator until I find out how to install the API package
wordDictionary = ["pickles",  "apples", "hunger", "tree", "technology", "purple", "stomach", "animation", "headphones", "father", "organic", " lavendar"]

#choosing random word
randomWord = random.choice(wordDictionary)
              
for x in randomWord:
    print("_", end= " ")