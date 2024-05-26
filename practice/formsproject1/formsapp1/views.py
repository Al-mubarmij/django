from django.shortcuts import render
from django.http import HttpResponse
from . import forms 
from .forms import ApplicationForm
# Create your views here.

def home(request):
    applicationform = forms.ApplicationForm()
    return render(request, 'templates/form.html', {'myform': applicationform})

def formdata(request):
    if request.method == 'POST':
        form = forms.ApplicationForm(request.POST)
        # check if it's valid
        if form.is_valid():
            name = form.cleaned_data['name']
            address = form.cleaned_data['address']
            field = form.cleaned_data['field']
            return HttpResponse('Successfully submitted')