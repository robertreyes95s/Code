from datetime import date
import re
from django.shortcuts import render
from spacexApp.models import futureLaunch
import requests

def index(request):
<<<<<<< HEAD
    return render(request, 'spacexApp/index.html')
=======
    return render(request, 'spacexApp/index.html')

def upcoming_launch(request):
    all_data = {}
    url = "https://api.spacexdata.com/v3/launches/upcoming/"
    response = requests.get(url)
    data = response.json()

    for d in data:
        space_data = futureLaunch(
            launch = d['launch_date_local']  
        )
        space_data.save()
        all_data = futureLaunch.objects.all().order_by('-id')

    return render(request, "spacexApp/index.html", {"all_data": all_data})
        
>>>>>>> c290fc2d5919fe19333c760347937fbd8f408691
