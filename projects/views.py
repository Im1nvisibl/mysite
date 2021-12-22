from django.shortcuts import render
from django.http import HttpResponse


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
    page = 'Projects'
    context = {'projects': projectsList}
    return render(request, 'projects/projects.html',context)

def project(request, pk):
    projectObj = None
    for i in projectsList:
        if i['id'] == pk:
            projectObj = i
    return render(request, 'projects/single-project.html', {'project': projectObj})
