# Python Pratice Problem - Rock Paper Scissors 
# this is a two player game
# python3
import getpass as gp
import time
import random

def game():
    player1_name = input("Enter a name for Player 1")
    player1 = player1_name

    rock = 1
    paper = 2
    scissors = 3

    turns =
    while turns < 3:
        player1_score = 0
        playerAI_score = 0

        choices_ai = [1, 2, 3]

        p1_choice = gp.getpass("Player 1 Choose: Rock[1], paper[2], or scissors[3]")
        ai_choice = random.choice(choices_ai)

        if p1_choice == 1 and ai_choice == 2:
            plater1_scroe += 1
            print("player1 wins" + p1_choice +  " beats " + ai_choice)
        else:
            prin("Nothing")


print("Hello, welcome to Rock Paper Scissors")
determine_game = input("Do you want to play?")
if determine_game == "Yes" or 'y' or "Y" or "YES" or "yes":
    game()
else:
    exit



