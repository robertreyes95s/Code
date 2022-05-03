# Python Pratice Problem - Rock Paper Scissors 
# this is a two player game
# python3
import time
import random

def game():
    player1_name = input("Enter a name for Player 1: ")
    player1 = player1_name

    turns = 0
    player1_score = 0
    ai_score = 0

    while turns < 3:

        choices_ai = [1, 2, 3]

        p1_choice = input(player1_name + " choose: Rock[1], paper[2], or scissors[3]\n")
        ai_choice = random.choice(choices_ai)

        if p1_choice == 1 and ai_choice == 1:
            turns += 1
            print("Draw")
        elif p1_choice == 1 and ai_choice == 2:
            print("Point to Ai Bob")
            ai_score += 1
            turn += 1 
        elif p1_choice == 1 and ai_choice == 3:
            print("Point to " + player1_name)
            player1_score += 1 
            turn += 1
        elif p1_choice == 2 and ai_choice == 1:
            print("Point to " + player1_name)
            player1_score += 1 
            turn += 1 
        elif p1_choice == 2 and ai_choice == 2: 
            turns  += 1 
            print("Draw")
        elif p1_choice == 2 and ai_choice == 3: 
            print("Paint to Ai bob")
            ai_score += 1
            turn += 1 
        elif p1_choice == 3 and ai_choice == 1: 
            print("Point to Ai Bob")
            ai_score += 1
            turn += 1
        elif p1_choice == 3 and ai_choice == 2: 
            print('Point to' + player1_name)
            player1_score += 1
            turns += 1
        elif p1_choice == 3 and ai_choice == 3:
            print("Draw")
            turns += 1 
        
    else: 
        print("Game Over")
    
    if player1_score < ai_choice: 
        print("Ai Bob Wins")
    else:
        print(player1_name + " Wins")

print("Hello, welcome to Rock Paper Scissors")
determine_game = input("Do you want to play?\n")
if determine_game == "Yes" or 'y' or "Y" or "YES" or "yes":
    game()
else:
    exit



