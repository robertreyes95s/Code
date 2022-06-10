# python practice
# find the longest word in a list 
# and then print the word and the 
# length of the word 

the_string = ["for", "final", "print", 'thefinalword']
longest = max(the_string, key=len)
print(longest)
print(len(longest))
    