from django.urls import path 
from . import views
urlpatterns = [
    path('app/', views.home, name="home"),
    path('', views.newthing, name=""),
    path('a', views.trying, name=""),
    
]