# Practice problem  
# inserting a string  in the middle of another string
# Python3!

def insert_mid(st, wrd): 
    lngth = len(st)
    mid = int(lngth) // 2
    print(st[mid:] + wrd + st[:mid]) 

string = "poolpool"
insert_mid(string, "fall")
