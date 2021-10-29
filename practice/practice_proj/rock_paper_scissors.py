import time
import sys

def game(): 
    rock = 1
    paper = 2
    scissors = 3

    print('Welcome to Rock Papper Sciccors')
    time.sleep(1)

    print("Enter yes/y or no/n play and or exit thte game")
    start_game = input()

    if start_game == "yes" or "y": 
        pass
    elif start_game == 'no' or 'n':
        sys.exit()

    player_one = input()
    player_two = input()


game()