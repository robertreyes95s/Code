import pandas as pd
import numpy as numpy
import seaborn as sns
import re
import time
from datetime import datetime 
from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests


url = "https://spotthestation.nasa.gov/sightings/view.cfm?country=United_States&region=California&city=Fremont#.YYyb8mCIaXJ"
html = urlopen(url)

soup = BeautifulSoup(html, 'lxml')
title = soup.title

rows = soup.find_all('tr')
for row in rows: 
    row_td = row.find_all('td')

str_cells = str(row_td)
cleantext = BeautifulSoup(str_cells, "lxml").get_text()
print(cleantext)


