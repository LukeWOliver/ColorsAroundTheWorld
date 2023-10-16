"""
Made by Vighnesh Koikal and Luke Oliver 10/13/23
Spanish module containg functions for quiz and questions
"""

import random, subprocess, sys

# Instantiate variables that will be used globally - LWO & VK
score = 0
missed_questions = []

# Get user's operating system - LWO
os = sys.platform

def Spanish():
    ### --- Setup --- ### - VK
    questions = [BlueQuestion, RedQuestion, GreenQuestion, YellowQuestion, PurpleQuestion, 
                 BrownQuestion, OrangeQuestion, BlackQuestion, WhiteQuestion, PinkQuestion]
    run = True
    retake = ""
    
    global score
    global missed_questions
    
    ### --- Teach the user --- ### - LWO
    print("Welcome to the spanish section.\n ")
    input("Colors in spanish are a little different than colors in English. Press ENTER to continue...")
    print("A lot of colors have direct translation, such as: ")
    print("Blue - Azul")
    print("Brown - Marron")
    print("Pink - Rosa")
    print("Orange - Naranja")
    print("Green - verde")
    input("Press ENTER to continue...")
    print("But some colors have multiple versions. One for male, and one for female. ")
    print("Such as: ")
    print("Color                Masculine                Feminine")
    print("------------------------------------------------------")
    print("Yellow               Amarillo                 Amarilla")
    print("White                Blanco                   Blanca  ")
    print("Black                Negro                    Negra   ")
    print("Purple               Morado                   Morada  ")
    print("Red                  Rojo                     Roja    ")
    input("Press ENTER to continue...")
    print("All colors also have slightly different words when refering to multiple (plural) things, ")
    print("but we will focus on singular versions of the words today. ")
    input("Press ENTER to continue...")
    print("Take a minute to familiarize yourself with these terms. ")
    
    ### --- Quiz Loop --- ### - LWO & VK
    while run:
        
        # Clear terminal (dependant on user's operating system) so that the user cannot cheat - LWO
        input("Press enter when you are ready to begin your quiz! ")
        if os == "win32":
            subprocess.run('cls', shell=True)
        elif os == "darwin" or os == "linux":
            subprocess.run('clear', shell=True)
        
        # Reset score and missed questions after each quiz - LWO & VK
        missed_questions = []
        score = 0
        
        # Give user character info - LWO
        print("Note that special symbols are not available and should not be used in this program.\n")
        
        # Shuffle the order of questions - LWO
        random.shuffle(questions)
        
        # Ask each question in the order of the shuffled list by itterating 
        # through the list (which contains function names) and calling the
        # function based on the index of the list and the iteration - LWO
        for question in range(len(questions)):
            questions[question](question + 1)
        
        # Print final score - LWO
        print("Your final score was... " + str(score) + "/10! ")
        
        # Print missed questions - LWO
        if score < 10:
            print("\nYou missed the following questions: ")
            for missed_question in range(len(missed_questions)):
                print(str(missed_questions[missed_question]))
        
        # Ask the user if they would like to retake the quiz, and break
        # the main loop if they would not like to retake - VK
        retake = str(input("\nWould you like to retake the quiz? ")).lower()
        if retake == "yes" or retake == "y" :
            continue
        else:
            run = False
            
# Function for blue question - LWO
def BlueQuestion(question_number):
    # Global score variable
    global score
    global missed_questions
    
    # Predetermined answer
    blue_answer = "blue"
    
    # Print question and obtain user input (answer)
    print("Question " + str(question_number) + ": ")
    blue_user_answer = str(input("What color is 'azul' in English? ")).lower()
    
    # If the user gets the question right, add to their score
    if blue_user_answer == blue_answer:
        score += 1
    else:
        missed_questions.append(question_number)
        
    # Create whitespace
    print()

# Function for red question - VK
def RedQuestion(question_number):
    # Global score variable
    global score
    global missed_questions
    
    # Predetermined answer
    red_answer = "red"
    
    # Print question and obtain user input (answer)
    print("Question " + str(question_number) + ": ")
    red_user_answer = str(input("What color is 'roja' in English? ")).lower()
    
    # If the user gets the question right, add to their score
    if red_user_answer == red_answer:
        score += 1
    else:
        missed_questions.append(question_number)
        
    # Create whitespace
    print()

# Function for green question - LWO
def GreenQuestion(question_number):
    # Global score variable
    global score
    global missed_questions
    
    # Predetermined answer
    green_answer = "verde"
    
    # Print question and obtain user input (answer)
    print("Question " + str(question_number) + ": ")
    green_user_answer = str(input("How do you say 'green' in Spanish? ")).lower()
    
    # If the user gets the question right, add to their score
    if green_user_answer == green_answer:
        score += 1
    else:
        missed_questions.append(question_number)
        
    # Create whitespace
    print()

# Function for yellow question - VK
def YellowQuestion(question_number):
    # Global score variable
    global score
    global missed_questions
    
    # Predetermined answer
    yellow_answer = "amarilla"
    yellow_answer2 = "amarillo"
    
    # Print question and obtain user input (answer)
    print("Question " + str(question_number) + ": ")
    yellow_user_answer = str(input("How do you say 'yellow' in Spanish? ")).lower()
    
    # If the user gets the question right, add to their score
    if yellow_user_answer == yellow_answer or yellow_user_answer == yellow_answer2:
        score += 1
    else:
        missed_questions.append(question_number)
        
    # Create whitespace
    print()

# Function for purple question - VK
def PurpleQuestion(question_number):
    # Global score variable
    global score
    global missed_questions
    
    # Predetermined answer
    purple_answer = "morada"
    purple_answer_2 = "morado"
    
    # Print question and obtain user input (answer)
    print("Question " + str(question_number) + ": ")
    purple_user_answer = str(input("How do you say 'purple' in Spanish? ")).lower()
    
    # If the user gets the question right, add to their score
    if purple_user_answer == purple_answer or purple_user_answer == purple_answer_2:
        score += 1
    else:
        missed_questions.append(question_number)
        
    # Create whitespace
    print()
    
# Function for brown question - LWO
def BrownQuestion(question_number):
    # Global score variable
    global score
    global missed_questions
    
    # Predetermined answer
    brown_answer = "b"
    
    # Print question and obtain user input (answer)
    print("Question " + str(question_number) + ": ")
    print("What is 'brown' in Spanish? ")
    print("A: Moreno ")
    print("B: Marron ")
    print("C: Amarillo ")
    print("D: Morena ")
    brown_user_answer = str(input("Enter either A, B, C, or D: ")).lower()
    
    # If the user gets the question right, add to their score
    if brown_user_answer == brown_answer:
        score += 1
    else:
        missed_questions.append(question_number)
        
    # Create whitespace
    print()
    
# Function for orange question - VK
def OrangeQuestion(question_number):
    # Global score variable
    global score
    global missed_questions
    
    # Predetermined answer
    orange_answer = "d"
    
    # Print question and obtain user input (answer)
    print("Question " + str(question_number) + ": ")
    print("What is 'orange' in Spanish? ")
    print("A: Roja")
    print("B: Amarillo")
    print("C: Verde")
    print("D: Naranja")
    orange_user_answer = str(input("Enter either A, B, C, D: ")).lower()
    
    # If the user gets the question right, add to their score
    if orange_user_answer == orange_answer:
        score += 1
    else:
        missed_questions.append(question_number)
        
    # Create whitespace
    print()

# Function for black question - VK
def BlackQuestion(question_number):
    # Global score variable
    global score
    global missed_questions
    
    # Predetermined answer
    black_answer = "c"
    
    # Print question and obtain user input (answer)
    print("Question " + str(question_number) + ": ")
    print("What is 'black' in Spanish? ")
    print("A: Blanca")
    print("B: Moreno")
    print("C: Negra")
    print("D: Roja")
    black_user_answer = str(input("Enter either A, B, C, D: ")).lower()
    
    # If the user gets the question right, add to their score
    if black_user_answer == black_answer:
        score += 1
    else:
        missed_questions.append(question_number)
        
    # Create whitespace
    print()

# Function for white question - VK
def WhiteQuestion(question_number):
    # Global score variable
    global score
    global missed_questions
    
    # Predetermined answer
    white_answer = "a"
    
    # Print question and obtain user input (answer)
    print("Question " + str(question_number) + ": ")
    print("What is 'white' in Spanish? ")
    print("A: Blanca")
    print("B: Verde")
    print("C: Azul")
    print("D: Amarillo")
    white_user_answer = str(input("Enter either A, B, C, D: ")).lower()
    
    # If the user gets the question right, add to their score
    if white_user_answer == white_answer:
        score += 1
    else:
        missed_questions.append(question_number)
        
    # Create whitespace
    print()

# Function for pink question - VK
def PinkQuestion(question_number):
    # Global score variable
    global score
    global missed_questions
    
    # Predetermined answer
    pink_answer = "b"
    
    # Print question and obtain user input (answer)
    print("Question " + str(question_number) + ": ")
    print("What is 'pink' in Spanish? ")
    print("A: Amarilla")
    print("B: Rosa")
    print("C: Roja")
    print("D: Rojo")
    pink_user_answer = str(input("Enter either A, B, C, D: ")).lower()
    
    # If the user gets the question right, add to their score
    if pink_user_answer == pink_answer:
        score += 1
    else:
        missed_questions.append(question_number)
        
    # Create whitespace
    print()
