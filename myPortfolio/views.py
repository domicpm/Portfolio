from django.shortcuts import render

# Create your views here.
def myportfolio(request):
    return render(request, 'portfolio.html')

def about(request):
    return render(request, 'about.html')

def projects(request):
    return render(request, 'projects.html')

def contact(request):
    return render(request, 'contact.html')

def arcanox(request):
    return render(request, 'arcanox.html')
