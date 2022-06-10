# Practice Problem - Python3
# For the first charcter in a string, change 
# all of the same charcter in the the string to 
# '$', except the first character

def change_char(strng):
    first = strng[0]
    replacer = '$'
    for s in strng:
        if s == first:
            strng = strng.replace(s, replacer)
    print(strng)

new_string = 'opoopertoer'
change_char(new_string)
