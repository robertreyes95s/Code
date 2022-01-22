#Not a pointer 
print('_______NOT A POINTER______')
num1 = 11

num2 = num1 

print('Before value is updated')
print('num1=', num1)
print('num2=', num2)

print()
num1 = 22
print("Changing value of 'num1' to 22")

print("\nAfter value is updated:")
print("num1 = ", num1)
print("num2 =", num2)

print()
print()

# Pointer Exmaple
print("_____POINTER EXMAPLE______")
dict1 = {
    'value': 11
}

dict2 = dict1

print("Before value is updated:")
print("dict1=", dict1)
print('dict1', dict2)

print()
dict1['value'] = 22
print("Changing calue of 'dict1' to 22")

print("\nAfter value is updated:")
print("dict1=", dict1)
print('dict1', dict2)