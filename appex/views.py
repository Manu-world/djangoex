from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse("this is home, and url")

def about(request):
    return HttpResponse("this is the about page")

def service(request):
    return HttpResponse("this is the service page")
