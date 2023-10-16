"""
Luke Oliver & Vighnesh Koikal 10/13/23      
This is the main script which controls which langauge module is engaged
using a function and function calls
"""

import spanish

# Function for the main/opening menu - LWO & VK
def Menu():
    language = ""
    languages = ["Spanish", "French"]
    
    # Print welcome message - LWO & VK
    print("Welcome to Colors Around the World!\n")
    print("This program aims to teach you the basics of different languages.")
    print("We currently have " + str(len(languages)) + " available  languages:\n")
    
    # Print each available language - LWO
    for i in range(len(languages)):
        print(languages[i])
    print()
    
    # While loop containing language selection that prevents
    # the program from crashing given an unusable input - LWO & VK
    while language != "spanish" and language != "french" and language != "quit":
        language = str(input("Please enter a language you would like to pracitce (if you would like to exit the program, type \"quit\"): ")).lower()

        # Check which language is chosen and run the function for said language - VK
        if language == "spanish":
            spanish.Spanish()
        elif language == "french":
            french.French()
        elif language == "quit":
            break
    
    # Create whitespace - LWO
    print()

Menu()

# The original plan was to reuse the menu function in the other language
# classes, but time ran out before this could be porperlly implemented
