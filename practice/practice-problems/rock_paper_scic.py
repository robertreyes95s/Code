# Python Pratice Problem - Rock Paper Scissors 
# this is a two player game
# python3
import getpass as gp
import time

def game(): 
    player1_name = input("Enter a name for Player 1")
    player2_name = input("Enter a name for Plater 2")

    player1 = player1_name
    player2 = player2_name

    turns = 0
    while turns < 3:
        player1_score = 0
        player2_score = 0

        p1_choice = gp.getpass("Player 1 Choose: Rock[1], paper[2], or scissors[3]")
        p2_choice = gp.getpass("Plater 2 Choose: Rock[1], paaper[2], or scissors[3]")

        if p1_choice == 1 and p2_choice == 2: 
            print(player2_name, "wins this round")
        elif p1_choice == 2 and p2_choice == 1 

        


print("Hello, welcome to Rock Paper Scissors")
determine_game = input("Do you wnat to play?")
if determine_game == "Yes" or 'y' or "Y" or "YES" or "yes":
    game()
else: 
    exit



