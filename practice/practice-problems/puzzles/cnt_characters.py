# Python practice problem 
# Couts the frequency of each charcter in a sting
# python3!

def count(str1):
    dict = {}
    for s in str1:
        keys = dict.keys
        if s in keys:
            dict[s] += 1
        else:
            dict[s] = 1
    return dict
print(count('youtubethefile'))

