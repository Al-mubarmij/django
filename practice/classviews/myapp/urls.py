from django.urls import path 
from . import views
from .views import NewView
urlpatterns = [
    path('index/', NewView.as_view(), name='index')
]