from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.

def index(request):
    return HttpResponse("This is index!")

def login(request):
    template = loader.get_template("form.html")
    context = {}
    return HttpResponse(template.render(context, request))