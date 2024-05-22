from django.shortcuts import render
from django.http import HttpResponse


def home(requst):
    return HttpResponse("welcome to little lemon")

