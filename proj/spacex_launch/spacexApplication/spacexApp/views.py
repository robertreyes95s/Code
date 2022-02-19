from datetime import date
import re
from django.shortcuts import render
from spacexApp.models import futureLaunch
import requests

def index(request):
    return render(request, 'spacexApp/index.html')
