from django.shortcuts import render
from .forms import BookFlight 
# Create your views here.
def book_flight(request):
    if request.method == 'POST':
        form = BookFlight(request.POST)
        if form.is_valid():
            form.save()
    form = BookFlight()
    context = {'bookingform': form}
    return render(request, 'templates/booking.html', context)