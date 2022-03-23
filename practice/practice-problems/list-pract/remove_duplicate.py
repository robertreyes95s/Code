# Python Procatice Problem 
# Remove duplicates from a list 

def remv_duplicate(lst):
    for n in lst: 
        if n == n: 
           lst.replace(n, " ")
    return lst

l = (1, 2, 2, 3, 4, 666, 666, 7, 8, 9, 9)
remv_duplicate(l)
