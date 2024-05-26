from django.http import HttpResponse # type: ignore
from django.shortcuts import render # type: ignore


def Home(request):
    #return HttpResponse("Hello, world ! Welcome to Django Home Page!")
    return render(request, 'website/index.html')

def About(request):
    #return HttpResponse("Hello, world ! Welcome to Django About Page!")
    return render(request, 'website/about.html')

def Contact(request):
    return render(request, 'website/contact.html')
    #return HttpResponse("Hello, world ! Welcome to Django Contact Page!")