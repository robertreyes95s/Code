# Pratice question 
# This program takes a list and swaps the first and last elements of the list
# Input : [12, 35, 9, 56, 24]
# Output : [24, 35, 9, 56, 12]

# Input : [1, 2, 3]
# Output : [3, 2, 1]

list = [1, 2, 3, 4, 6, 7]

def swap(list):
    for i in str(list): 
        first = i[0]
        last = i[-1]
        list[0] = last
        list[-1] = first 
        print(list)
swap(list)

# still needs work
