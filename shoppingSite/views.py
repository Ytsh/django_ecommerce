from django.shortcuts import render

# Create your views here.

def homepage(request):
    return render(request,'mainPage.html')

def mainPage(request):
    return render(request,'mainPage.html')

def contactUs(request):
    return render(request,'contactUs.html')

def aboutUs(request):
    return render(request,'aboutUs.html')

