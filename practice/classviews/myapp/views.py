from django.shortcuts import render
from django.views import View 
# Create your views here.
def index(request):
    return render(request, 'index.html', {})

class NewView(View):
    def get(self, request):
        return render(request, 'index.html', {})