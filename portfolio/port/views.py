from django.shortcuts import render
from . models import *
def index(request):
    projects = Project.objects.all()
    return render(request, 'index.html', {"projects" : projects})
