from django.shortcuts import render
from django.http import HttpResponse

from . import forms 


# Create your views here.
def signup(request):
    form = forms.Signup()
    return render(request, 'templates/signup.html', {'signupform': form} )

def userdata(request):
    if request.method == "POST":
        form = forms.Signup(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            return HttpResponse('Welcome ' + name)