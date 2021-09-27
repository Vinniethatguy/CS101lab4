print("Welcome to Flarsheim Guesser!")
choice='y'
########################################################################
##
## CS 101 Lab
## Program #
## Name: Vince Smith
## Email vasy9z@umsystem.edu
##
## PROBLEM : Describe the problem
## I am creating an algorithm that determaines a persons number with the use of loops, if statements and modulus
## The modulus method checks a remainder, for the numbers 1-100. So we are asking the user whats the remainder of their number
## by 3,5, and 7
## ALGORITHM : 
##      1. Write out the algorithm
## 
## ERROR HANDLING:
##      Any Special Error handling to be noted.  Wager not less than 0. etc
##
## OTHER COMMENTS:
##      Any special comments
##
########################################################################

while(choice == 'Y' or choice == 'y'):
    print("\nPlease think of a number between and including 1 and 100.")
        
    r3 = int(input("What is the remainder when your number is divided by 3  "))
    r5 = int(input("What is the remainder of your number when its divided by 5?  "))
    r7 = int(input("What is the remainder when your number is divided by 7?  "))
        
    while r3 < 0 or r3 > 3:
        if r3 < 0:
            print("The integer must be greater than 0")
        else:
            print("The integear must be less than 3")
                
        r3 = int(input("What is the remainder when your number is divided by 3?  "))
            
    
    while r5 < 0 or r5 > 5:
        if r5 < 0:
            print("The integer must be greater than 0")
        else:
            print("The integear must be less than 5")
            
            r5 = int(input("What is the remainder of your number when its divided by 5? "))
        
    while r7 < 0 or r7 > 7:
        if r7 < 0:
            print("The integear must be greater than 0")
        else:
            print("The integear must be less than 7")
        
            r7 = int(input("What is the remainder when your number is divided by 7? "))
            
    for i in range(1,101):
        if i%3 == r3 and i%5 == r5 and i%7 == r7:
            print(f"Your number is {i}")
            print("How azaming is that?\n")
            
            
    choice = input("Do you want to play again?")        
    while(choice != 'Y' and choice != 'N' and choice != 'y' and choice != 'n' ):
        
        choice =input("Do you want to play again? Y to continue,N to quit ==>")
