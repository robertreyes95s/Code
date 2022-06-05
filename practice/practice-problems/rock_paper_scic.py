# Python Pratice Problem - Rock Paper Scissors 
# this is a two player game
# python3
import random

def game():
    player1_name = input("Enter a name: ")
    
    turns = 0
    player1_score = 0
    ai_score = 0
    choices_ai = [1, 2, 3]

    while turns < 3:

        choice = input(player1_name + " choose: Rock[1], paper[2], or scissors[3]\n")
        ai_choice = random.choice(choices_ai)

        p1_choice = int(choice)

        if p1_choice == 1 and ai_choice == 1:
            turns += 1
            print("Draw")
            print("p1 score: " + str(player1_score))
            print("ai score: " + str(ai_score)+ "\n")
            print("ai chose Rock")
        elif p1_choice == 1 and ai_choice == 2:
            print("Point to Ai Bob")
            ai_score += 1
            turns += 1 
            print("p1 score: " + str(player1_score))
            print("ai score: " + str(ai_score)+ "\n") 
            print("ai chose Paper")                  
        elif p1_choice == 1 and ai_choice == 3:
            print("Point to " + player1_name)
            player1_score += 1 
            turns += 1
            print("p1 score: " + str(player1_score))
            print("ai score: " + str(ai_score)+ "\n") 
            print("ai chose Scissors")       
        elif p1_choice == 2 and ai_choice == 1:
            print("Point to " + player1_name)
            player1_score += 1 
            turns += 1
            print("p1 score: " + str(player1_score))
            print("ai score: " + str(ai_score))           
        elif p1_choice == 2 and ai_choice == 2: 
            turns  += 1 
            print("Draw")
            print("p1 score: " + str(player1_score))
            print("ai score: " + str(ai_score))        
        elif p1_choice == 2 and ai_choice == 3: 
            print("Paint to Ai bob")
            ai_score += 1
            turns += 1 
            print("p1 score: " + str(player1_score))
            print("ai score: " + str(ai_score))
        elif p1_choice == 3 and ai_choice == 1: 
            print("Point to Ai Bob")
            ai_score += 1
            turns += 1
            print("p1 score: " + str(player1_score))
            print("ai score: " + str(ai_score))
        elif p1_choice == 3 and ai_choice == 2: 
            print('Point to ' + player1_name)
            player1_score += 1
            turns += 1
            print("p1 score: " + str(player1_score))
            print("ai score: " + str(ai_score))
        elif p1_choice == 3 and ai_choice == 3:
            print("Draw")
            turns += 1 
            print("p1 score: " + str(player1_score))
            print("ai score: " + str(ai_score))
        else: 
            print("Enter Valid Response")
        
    else: 
        print("Game Over\n")
        print("p1 score: " + str(player1_score))
        print("ai score: " + str(ai_score))
    
    if player1_score < ai_score: 
        print("Ai Bob Wins")
    else:
        print(player1_name + " Wins")
print()
print("Hello, Welcome to Rock Paper Scissors\n")
determine_game = input("Do you want to play?\n")
if determine_game == "Yes" or 'y' or "Y" or "YES" or "yes":
    game()
else:
    exit



