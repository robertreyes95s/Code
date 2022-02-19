# Practice problem 
# Take the first two and last two charcters 
# of a string and ake on word with it
# python3! 

def make_word(str1):
    first_two = str1[:2]
    last_two = str1[-2:]
    print(first_two + last_two)

str2 = input("Please enter a string\n")
print(make_word(str2))


