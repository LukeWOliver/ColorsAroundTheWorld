## French Game Code ##

import random, subprocess, sys

#Global Variables
score = 0
missed_questions =[]

# Get user's operating system
os = sys.platform

def French():
    questions = [BlueQ, RedQ, WhiteQ, GreyQ, BrownQ, PinkQ, BlackQ, PurpleQ, OrangeQ, GreenQ]
    Run = True
    retake = ""
    
    global score
    global missed_questions

    
##Input/Question ##
    print("You have reached the french section. \n")
    input("Colors in French are a bit diffent than the ones in English. Press ENTER to countine")
    print("Many colors have direct translation, examples being: ")
    print("Blue - Bleu")
    print("Green - Vert")
    print("Pink - Rose")
    print("Red - Rouge")
    print("Black - Noir")
    print("But some colors have multiple versions. One for male, and one for female. ")
    print("Such as: ")
    print("Color                Masculine                Feminine")
    print("------------------------------------------------------")
    print("Grey                   Gris                      Grise")
    print("Purple	              Violet	             Violette")
    print("White	              Blanc	                  Blanche")
    print("Black	              noirs	                    noire")
    print("Brown	              bruns	                    brune")
    ### Qiuz Loop ###  
    while Run:
        
        # Clear terminal (dependant on user's operating system) so that the user cannot cheat
        print("You have reached the french section, try your best to translate the following words")
        input("Please press enter when you are ready to start the quiz")
        if os == "win32":
            subprocess.run('cls', shell = True)
        elif os == "darwin" or os == "linux":
            subprocess.run('clear', shell= True)
        
        #Reset score when questions are missed
        missed_questions = []
        score = 0
        
        #Give user character info
        print("Note that special symbols are not available and should not be considered for this test")
        
        ### Shuffel the order of questions ###
        random.shuffle(questions)
        
        #Ask each question in order of the list
        for question in range(len(questions)):
            questions[question](question + 1)
            
        #print final score
        print("Your final score was.." + str(score) + "/10" )
        
        #print missed questions
        if score < 10:
            print("\nYou missed the following questions: ")
            for missed_question in range(len(missed_questions)):
                print(str(missed_questions[missed_question]))
                
        # Ask the user if they would like to retake the quiz, and break
        # the main loop if they would not like to retake
        retake = str(input("\nWould you like to retake the quiz? ")).lower()
        if retake == "yes" or retake == "y" :
            continue
        else:
            run = False

def BlueQ(question_number):
    # Global score variable
    global score
    global missed_questions
    
    #Predetermined answer
    blue_answer = "blue"
    
    # Print question and obtain user input (answer)
    print("Question " + str(question_number) + ": ")
    blue_user_answer = str(input("What color is 'bleu' in English? ")).lower()
    
    # If the user gets the question right, add to their score
    if blue_user_answer == blue_answer:
        score += 1
    else:
        missed_questions.append(question_number)
        
    # Create whitespace
    print()
    
def RedQ(question_number):
    # Global score variable
    global score
    global missed_questions
    
    # Predetermined answer
    red_answer = "red"
    
    # Print question and obtain user input (answer)
    print("Question " + str(question_number) + ": ")
    red_user_answer = str(input("What color is 'Rouge' in English? ")).lower()
    
    # If the user gets the question right, add to their score
    if red_user_answer == red_answer:
        score += 1
    else:
        missed_questions.append(question_number)

def GreenQ(question_number):
    # Global score variable
    global score
    global missed_questions
    
    # Predetermined answer
    green_answer = "Vert"
    
    # Print question and obtain user input (answer)
    print("Question " + str(question_number) + ": ")
    green_user_answer = str(input("How do you say 'green' in French? ")).lower()
    
    # If the user gets the question right, add to their score
    if green_user_answer == green_answer:
        score += 1
    else:
        missed_questions.append(question_number)
        
    # Create whitespace
    print()
def PurpleQ(question_number):
    # Global score variable
    global score
    global missed_questions
    
    # Predetermined answer
    purple_answer = "violet"
    purple_answer_2 = "violette"
    
    # Print question and obtain user input (answer)
    print("Question " + str(question_number) + ": ")
    purple_user_answer = str(input("How do you say 'purple' in French? ")).lower()
    
    # If the user gets the question right, add to their score
    if purple_user_answer == purple_answer or purple_user_answer == purple_answer_2:
        score += 1
    else:
        missed_questions.append(question_number)
        
    # Create whitespace
    print()
    
def BrownQ(question_number):
    # Global score variable
    global score
    global missed_questions
    
    # Predetermined answer
    brown_answer = "A"
    
    # Print question and obtain user input (answer)
    print("Question " + str(question_number) + ": ")
    print("What is 'pink' in French? ")
    print("A: Rose ")
    print("B: Vert ")
    print("C: Brune ")
    print("D: Bleu ")
    brown_user_answer = str(input("Enter either A, B, C, or D: ")).lower()
    
    # If the user gets the question right, add to their score
    if brown_user_answer == brown_answer:
        score += 1
    else:
        missed_questions.append(question_number)
        
    # Create whitespace
    print()
def OrangeQ(question_number):
    # Global score variable
    global score
    global missed_questions
    
    # Predetermined answer
    orange_answer = "d"
    
    # Print question and obtain user input (answer)
    print("Question " + str(question_number) + ": ")
    print("What is 'orange' in French? ")
    print("A: Rouge")
    print("B: Blanch")
    print("C: Noir")
    print("D: Orange")
    orange_user_answer = str(input("Enter either A, B, C, D: ")).lower()
    
    # If the user gets the question right, add to their score
    if orange_user_answer == orange_answer:
        score += 1
    else:
        missed_questions.append(question_number)
        
    # Create whitespace
    print()
    
def BlackQ(question_number):
    # Global score variable
    global score
    global missed_questions
    
    # Predetermined answer
    black_answer = "c"
    
    # Print question and obtain user input (answer)
    print("Question " + str(question_number) + ": ")
    print("What is 'black' in French? ")
    print("A: Rose")
    print("B: Vilotte")
    print("C: Noir")
    print("D: Blanch")
    black_user_answer = str(input("Enter either A, B, C, D: ")).lower()
    
    # If the user gets the question right, add to their score
    if black_user_answer == black_answer:
        score += 1
    else:
        missed_questions.append(question_number)
        
    # Create whitespace
    print()
def WhiteQ(question_number):
    # Global score variable
    global score
    global missed_questions
    
    # Predetermined answer
    white_answer = "blanc"
    white_answer_2 = "blanche"
    
    # Print question and obtain user input (answer)
    print("Question " + str(question_number) + ": ")
    white_user_answer = str(input("How do you say 'white' in French? ")).lower()
    
    # If the user gets the question right, add to their score
    if white_user_answer == white_answer or white_user_answer == white_answer_2:
        score += 1
    else:
        missed_questions.append(question_number)
        
    # Create whitespace
    print()
def PinkQ(question_number):
    # Global score variable
    global score
    global missed_questions
    
    # Predetermined answer
    pink_answer = "b"
    
    # Print question and obtain user input (answer)
    print("Question " + str(question_number) + ": ")
    print("What is 'black' in French? ")
    print("A: Bleu")
    print("B: Rose")
    print("C: Vert")
    print("D: Blanch")
    black_user_answer = str(input("Enter either A, B, C, D: ")).lower()
    
    # If the user gets the question right, add to their score
    if black_user_answer == pink_answer:
        score += 1
    else:
        missed_questions.append(question_number)
    # Create whitespace
    print()
def GreyQ(question_number):
    # Global score variable
    global score
    global missed_questions
    
    # Predetermined answer
    grey_answer = "Gris"
    grey_answer_2 = "Grise"
    
    # Print question and obtain user input (answer)
    print("Question " + str(question_number) + ": ")
    grey_user_answer = str(input("How do you say 'grey' in French? ")).lower()
    
    # If the user gets the question right, add to their score
    if grey_user_answer == grey_answer or grey_user_answer == grey_answer_2:
        score += 1
    else:
        missed_questions.append(question_number)
        
    # Create whitespace
    print()
    