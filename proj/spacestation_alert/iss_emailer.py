import csv 
import pandas as pd 
import time 
from datetime import datetime
import time

#csv section
file = open('iss_overhead_data.csv', 'r')
csvreader = csv.reader(file)
listData = list(csvreader)

one = listData[1][0]
two = listData[2][0]
three = listData[3][0]
four = listData[4][0]
five = listData[5][0]
six = listData[6][0]
seven = listData[7][0]
eight = listData[8][0]
nine = listData[9][0]
ten = listData[10][0]
eleven = listData[11][0]
twelve = listData[12][0]
thirteen = listData[13][0]
forteen = listData[14][0]
fiften = listData[15][0]
sixteen = listData[16][0]

dates = [one, two, three, four, five, six, seven, eight, nine, ten, eleven, twelve, thirteen, forteen, fiften, sixteen]

now = datetime.now()
time_now = now.strftime("%a %b %d, %I:%M %p")

print(time_now)
print(sixteen)

for d in dates: 
    if time_now != d: 
      continue
    else: 
        print(d)

    
    
    





