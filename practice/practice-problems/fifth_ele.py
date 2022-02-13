def fnd_fifth(lis):
    list_total = 0 
    threes = 0
    fifth = lis[5]
    for i in lis: 
        list_total = list_total + 1
        if i == 3: 
            fifth = fifth + 1
        else: 
            pass
    if list_total == 8 and fifth == 3:
        print("True")
    else: 
        print("False")
liss = [1, 2, 3, 4, 5, 5, 5, 4]
fnd_fifth(liss) 
        

        
