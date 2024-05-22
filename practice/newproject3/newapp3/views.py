from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    content = '<h1> Welcome to Little Lemon </h1>'
    return HttpResponse(content)

def trying(request):
    content = '<h1>good assumption!</h1>'
    return HttpResponse(content)


def newthing(request):
    content = '<h1>new assumption!</h1>'
    return HttpResponse(content)
