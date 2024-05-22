from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

'''def showform(request):
    return render(request, "form.html")
'''
def pathview(request, name, id):
    return HttpResponse("Name:{} UserID:{}".format(name, id*2))

def qryview(request):
    name = request.GET['name']
    id = request.GET['id']
    return HttpResponse("Name:{} UserID:{}".format(name, id))

def home(request):
    path = request.path
    scheme = request.scheme
    method = request.method 
    address = request.META['REMOTE_ADDR']
    user_agent = request.META['HTTP_USER_AGENT']
    path_info = request.path_info
    response = HttpResponse()
    response.headers['Age'] = 20
    msg = [f'''
                <br>Path: {path}
                <br>Address: {address}
                <br>Scheme: {scheme}
                <br>Method: {method}
                <br>User agent: {user_agent}
                <br>Path info: {path_info}
                <br> Response header: {response.headers}
        '''

    ]

    return HttpResponse(msg, content_type="text/html", charset="utf-8")