from django.shortcuts import render
from django.http import HttpResponse
from .models import Project


projectsList = [
    {
        'id':'1',
        'title':"Apple1",
        'description':'Is the best company'
    },
    {
        'id':'2',
        'title':"Apple2",
        'description':'Is the best company'
    },
    {
        'id':'3',
        'title':"Apple3",
        'description':'Is the best company'
    },
]

def projects(request):
    projects = Project.objects.all()
    context = {'projects': projects}
    return render(request, 'projects/projects.html',context)

def project(request, pk):
    projectObj = Project.objects.get(id=pk)
    return render(request, 'projects/single-project.html', {'project': projectObj})
