# this is a random password generator
import random 
import pyinputplus as pyip


def pass_random(): 

    # All characters that make passwords are generated from 
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    alpha_cap = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    special_car = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '+', '{', '}', '[', ']', '<', '>', '?']

    #All characters combined in one pool 
    all_characters = numbers + alpha + alpha_cap + special_car

    # Next up sort it so you can have choices wether to haev upercase or no uppercase, no special character, or only lettter no numbers 
    # and all those combintions of them

    #Final Password string
    password = ""

    #Length of password determinded by the user 
    choice = input("Length of password? - no longer than 15 charachters\n")

    #Generator of passwords
    if int(choice) <= 15:
        for i in range(int(choice)):
            cho = random.choice(all_characters)
            password += str(cho)
        else: 
            print(password)        
    else:
        print("Count to high")


print("Random Password Generator\n")

action = pyip.inputYesNo("Generate password? (yes or no) \n")
if action == 'yes': 
    pass
elif action == 'no': 
    exit()
else: 
    exit()
pass_random()