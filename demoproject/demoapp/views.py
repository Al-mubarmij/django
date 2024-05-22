from django.shortcuts import render
from django.http import HttpResponse 
# Create your views here.

def index(requiest):
    return HttpResponse("Hi this is the index of the demoapp")