import requests 
import json 

response = requests.get("https://api.spacexdata.com/v4/launches/upcoming-launches")
data = response.text
parse = json.loads(data)
print(parse)
