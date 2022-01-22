from django.shortcuts import render
from projects.models import Project

# Create your views here.
def project_index(request):
    projects = Project.objects.all()
    context = {
        'projects': projects
    
    }
    return render(request, 'project_index.html', context)

def project_details(requests, pk): 
    project = Project.objects.get(pk=pk)
    contect = {
        'project': project
    }
    return arender(request, 'project_details.html', context)