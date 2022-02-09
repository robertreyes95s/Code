# Practice Question
# This code finds the length of a list
# Python3 ~/code/practice/practice-questions

def length(list):
    total = 0 
    for l in list:
        total = total + 1  
    print(total) 
        
string_one = [1, 2, 3, 4, 2, 4, 2, 4, 5]
length(string_one)