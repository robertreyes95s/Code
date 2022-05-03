# this is a random password generator
import random 

def pass_random(): 
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    alpha_cap = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    all_characters = numbers + alpha + alpha_cap
    print(all_characters)
    choice = input("Length of password? - no longer than 15 charachters")
    if choice <= 15: 
        pass
    else: 
        exit()

    password = 

    


print("Random Password Generator\n")

action = input("Generate password?\n")
if action == 'y': 
    pass
elif action == 'n': 
    exit()
else:
    pass

pass_random()


