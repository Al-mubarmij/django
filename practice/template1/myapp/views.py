from django.shortcuts import render
from django.http import HttpResponse
from .forms import MessageForm

# Create your views here.
def index(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
    form = MessageForm()
    context = {'messageform': form}
    return render(request, 'myapp/templates/message.html', context)