# Python practice 
# Wrtie python program to scan specified directory
# and identify th edub directroires and files

import os
import time

path = input("PLease enter path: ")
os.system("ls -R " +  str(path))

