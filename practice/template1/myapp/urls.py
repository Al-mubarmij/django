from django.urls import path 
from . import views 


urlpatterns = [
    path('home/<str:name>', views.index, name='home'),
    path('hello/loader', views.hello_loader, name='hello'),
    path('render/<str:name>', views.hello_render, name="index")
]