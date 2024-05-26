from django.shortcuts import render
from . import forms 
# Create your views here.
def book_form(request):
    if request.method == 'POST':
        form = forms.BookingForm(request.POST)
        if form.is_valid():
            form.save()
    
    form = forms.BookingForm()
    context = {'booking_form': form}
    return render(request, 'templates/home.html', context)


