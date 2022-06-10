# Practice Problem - Exercise 1 in Condtions and Loops section
# Find the numbers that are divisble by 7 and multiple of  5
# Between 1500 and 2700 

number = range(1500, 2700)
def divisible_multples(rng):
    for n in rng: 
        if n % 7 == 0 and n % 5 == 0: 
            print(n) 
divisible_multples(number)

