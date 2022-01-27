from datetime import date
import re
from django.shortcuts import render
from spacexApp.models import futureLaunch
import requests

def index(request):
    return render(request, 'spacexApp/index.html')

def upcoming_launch(request):
    url = "https://api.spacexdata.com/v3/launches/upcoming"
    response = requests.get(url)
    data = response.json()
    return render(request, "spacexApp/index.html", {"data": data})
        
