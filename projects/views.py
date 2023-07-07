from django.shortcuts import render

projectsList = [
    {
        'id': '1',
        'title': 'Ecommerce Website',
        'description': 'Fully functional ecommerce website'
    },
    {
        'id': '2',
        'title': 'Portfolio Website',
        'description': 'A personal website to write articles and display work'
    },
    {
        'id': '3',
        'title': 'Social Network',
        'description': 'An open source project built by the community'
    }
]

# Create your views here.
def projects(request):
    context = {'projects': projectsList}
    return render(request,'projects/projects.html',context)

def project(request,pk):
    proj=None
    for i in projectsList:
        if i['id'] == pk:
            proj = i

    context = {'project':proj}
    return render(request,'projects/single_projects.html',context)



