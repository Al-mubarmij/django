from django.http import HttpResponseNotFound

def handler404(request, exception):
    return HttpResponseNotFound("Not Fa")