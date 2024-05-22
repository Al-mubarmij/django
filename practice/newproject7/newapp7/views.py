from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def display_menu_item(request, item):
    return HttpResponse("This is it" + item )