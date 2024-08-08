from django.shortcuts import render

# Create your views here.

def homepage(request):
    return render(request,'base.html')

def mainPage(request):
    return render(request,'mainPage.html')
