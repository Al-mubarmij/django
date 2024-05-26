from django.shortcuts import render
from .forms import LogForm
# Create your views here.
#from .forms import InputForm

def form_view(request):
    form = LogForm()
    if request.method == 'POST':
        form = LogForm(request.POST)
        if form.is_valid():
            form.save()

    context = {"form": form}
    return render(request, 'templates/home.html', context)