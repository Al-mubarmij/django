from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime 
# Create your views here.
def say_hello(request):
    return HttpResponse("hello world")

def homepage(request):
    return HttpResponse("Welcome to little Lemon!")

def display_date(request):
    date_joined = datetime.today().year
    return HttpResponse(date_joined)

def menu(request):
    text = '<h1 style="color:#F3AE12;"> This is the menu</h1>'
    return HttpResponse(text)