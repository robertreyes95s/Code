# Python practie - Python3
# Find the largest number in a list 

def find_large(lst):
    for i in lst:
        if i >= max(lst):
            print(i)

list = [123, 323, 33, 12, 5345, 33]
find_large(list)