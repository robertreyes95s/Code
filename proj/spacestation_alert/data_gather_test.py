import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as numpy
import seaborn as sns
import re
import time
from datetime import datetime 
from urllib.request import urlopen
import re

page = requests.get("https://spotthestation.nasa.gov/sightings/view.cfm?country=United_States&region=California&city=Fremont#.YYyb8mCIaXJ")
soup = BeautifulSoup(page.content, 'html.parser')

results = soup.find("div", class_="table-responsive")

job_elements = results.find("table", class_="table table-striped table-condensed table-hover table-bordered")

list_rows = []
for data in job_elements:
    cells = data.find('td')
    str_cells = str(cells)
    clean = re.compile('<.*?>')
    clean2 = (re.sub(clean, '', str_cells))
    list_rows.append(clean2)
print(clean2)
    