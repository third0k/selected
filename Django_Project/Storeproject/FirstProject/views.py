from django.shortcuts import render
from django.http import HttpResponse

def Home(request):
    return render(request,'index.html')

def about(request):
    return render(request,'aboutour.html')

def contact(request):
    return render(request,'contact.html')

def dogfood(request):
    return render(request,'dogfood.html')

def dogtoy(request):
    return render(request,'dogtoy.html')

def catfood(request):
    return render(request,'catfood.html')

def cattoy(request):
    return render(request,'cattoy.html')

def log(request):
    return render(request,'log.html')

