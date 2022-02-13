def fnd_match(lis):
    nineteens = 0
    fives = 0
    for i in lis:
        if i == 9: 
            nineteens += 1
        elif i == 5: 
            fives += 1
        else:
            pass

    if nineteens == 2 and fives >= 3: 
        print("True")
    else: 
        print("False")

the_list = [9, 3, 2, 5, 9, 5, 5, 5, 5]
fnd_match(the_list)

second_list = [9, 2, 3, 4, 2, 3, 5, 6]
fnd_match(second_list)
