# This programs i a practice problem from practicepython.org
# Odd Or Even

number= input("Please enter a number: ")
divone = float(number) % 2

if float(number) % 2 == 0:
    print("Woah that's an even number")
elif float(number) % 1 == 0:
    print("tha's an od dnumber")
else:
    print("That's not a number")


