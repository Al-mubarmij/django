from django.shortcuts import render
from django.http import HttpResponse
from .forms import MessageForm
from django.template import loader
# Create your views here.

# using template loader | Does the same as render
def hello_loader(request):
    template = loader.get_template('hello.html')
    context = {}
    return HttpResponse(template.render(context, request))

# Using render

def hello_render(request, name):
    context = {'name': name}
    return render(request,'myapp/templates/hello.html', context)

def index(request, name):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
    form = MessageForm()
    context = {'messageform': form}
    #return render(request, 'myapp/templates/message.html', context)
    return HttpResponse("<h1>Hello, {}. </h1>".format(name))