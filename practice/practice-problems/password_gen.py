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
    #all_characters = numbers + alpha +  alpha_cap +  special_car

    # Next up sort it so you can have choices wether to haev upercase or no uppercase, no special character, or only lettter no numbers 
    # and all those combintions of them

    #Final Password string
    password = ""

    #Length of password determinded by the user 
    length_choice = pyip.inputInt("Length of password? - no longer than 15 charachters\n", min=1, max=17)
    alph_cap_choice = pyip.inputYesNo("Include captilized alpha characters?\n")
    alpha_choice = pyip.inputYesNo("Inlcude lower case alpha characters?\n")
    special_char_choice = pyip.inputYesNo('Include special characters?\n')
    num_choice = pyip.inputYesNo('Include numbers?\n')



    #Generator of passwords
    if int(length_choice) <= 15 and alph_cap_choice == "yes" and alpha_choice == "yes" and special_char_choice == "yes" and num_choice == "yes":
        all_characters = numbers + alpha + alpha_cap + special_car
        for i in range(int(length_choice)):
            cho = random.choice(all_characters)
            password += str(cho)
        else:
            print(password) 

    if int(length_choice) <= 15 and alph_cap_choice == "no" and alpha_choice == "yes" and special_char_choice == "yes" and num_choice == "yes":
        all_characters = numbers + alpha + special_car
        for i in range(int(length_choice)):
            cho = random.choice(all_characters)
            password += str(cho)
        else: 
            print(password)

    if int(length_choice) <= 15 and alph_cap_choice == "yes" and alpha_choice == "no" and special_char_choice == "yes" and num_choice == "yes":
        all_characters = numbers + alpha_cap + special_car
        for i in range(int(length_choice)): 
            cho = random.choice(all_characters)
            password += str(cho)
        else: 
            print(password)

    if int(length_choice) <= 15 and alph_cap_choice == "yes" and alpha_choice == "yes" and special_char_choice == "no" and num_choice == "yes":
        all_characters = numbers + alpha + alpha_cap
        for i in range(int(length_choice)): 
            cho = random.choice(all_characters)
            password += str(cho)
        else: 
            print(password)

    if int(length_choice) <= 15 and alph_cap_choice == "yes" and alpha_choice == "yes" and special_char_choice == "yes" and num_choice == "no":
        all_characters = alpha + alpha_cap + special_car
        for i in range(int(length_choice)): 
            cho = random.choice(all_characters)
            password += str(cho)
        else: 
            print(password)

    if int(length_choice) <= 15 and alph_cap_choice == "no" and alpha_choice == "no" and special_char_choice == "yes" and num_choice == "yes":
        all_characters = special_car + numbers
        for i in range(int(length_choice)): 
            cho = random.choice(all_characters)
            password += str(cho)
        else: 
            print(password)

    if int(length_choice) <= 15 and alph_cap_choice == "yes" and alpha_choice == "yes" and special_char_choice == "no" and num_choice == "no":
        all_characters = alpha_cap + alpha
        for i in range(int(length_choice)): 
            cho = random.choice(all_characters)
            password += str(cho)
        else: 
            print(password)

    if int(length_choice) <= 15 and alph_cap_choice == "no" and alpha_choice == "no" and special_char_choice == "no" and num_choice == "yes":
        all_characters = numbers
        for i in range(int(length_choice)): 
            cho = random.choice(all_characters)
            password += str(cho)
        else: 
            print(password)

    if int(length_choice) <= 15 and alph_cap_choice == "yes" and alpha_choice == "no" and special_char_choice == "no" and num_choice == "no":
        all_characters = alpha_cap
        for i in range(int(length_choice)): 
            cho = random.choice(all_characters)
            password += str(cho)
        else: 
            print(password)

    if int(length_choice) <= 15 and alph_cap_choice == "no" and alpha_choice == "yes" and special_char_choice == "yes" and num_choice == "no":
        all_characters = alpha + special_car
        for i in range(int(length_choice)): 
            cho = random.choice(all_characters)
            password += str(cho)
        else: 
            print(password)

    if int(length_choice) <= 15 and alph_cap_choice == "yes" and alpha_choice == "no" and special_char_choice == "no" and num_choice == "yes":
        all_characters = alpha_cap + numbers
        for i in range(int(length_choice)): 
            cho = random.choice(all_characters)
            password += str(cho)
        else: 
            print(password)

    if int(length_choice) <= 15 and alph_cap_choice == "yes" and alpha_choice == "no" and special_char_choice == "yes" and num_choice == "no":
        all_characters = alpha_cap + special_car
        for i in range(int(length_choice)): 
            cho = random.choice(all_characters)
            password += str(cho)
        else: 
            print(password)

    if int(length_choice) <= 15 and alph_cap_choice == "no" and alpha_choice == "yes" and special_char_choice == "no" and num_choice == "yes":
        all_characters = alpha + numbers
        for i in range(int(length_choice)): 
            cho = random.choice(all_characters)
            password += str(cho)
        else: 
            print(password)
    
print("Random Password Generator\n")

action = pyip.inputYesNo("Generate password? (yes or no) \n")
if action == 'yes': 
    pass
elif action == 'no': 
    exit()
else: 
    exit()
pass_random()