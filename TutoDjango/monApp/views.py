from django.shortcuts import render
from django.http import HttpResponse


def home2(request):
        return HttpResponse("<h1>Hello DJANGO")

def home(request, param):
    return HttpResponse("<h1>Hello " + param + "</h1>")

def contact(request):
    return HttpResponse("<h1>Contact us</h1>")

def about(request):
    return HttpResponse("<h1>About us</h1>")