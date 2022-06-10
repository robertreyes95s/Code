# Practice Problem 
# list OS information and files in current dir 
# raise error if invalid or inaccessible
# file names and paths

import os
import time

# System Info 
operating_sys = os.system("uname -o")
kernel = os.system("uname -s")
kernel_version = os.system("uname -r")
kernal_relaese = os.system("uname -v")
processoor = os.system("uname -p")
hostname = os.system("uname -n")

# File dir 
current_dir = os.system("pwd")
directory = os.system("ls -la")

print("You wish to know about this system good sir?")
answer = input()

if answer == "yes" or "y" or "Y" or "YES" or "Yes":
    pass
elif answer == "No" or "n" or "N" or "no":
    print("As you wish, please come back when you have timee")
else:
    print("That is not a valid response... TRY AGAIN")
    exit()

time.sleep(1)
print("Gathering info..")
time.sleep(1.5)





