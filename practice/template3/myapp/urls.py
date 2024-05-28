from django.urls import path 
from . import views 

urlpatterns = [
    path('menu/', views.menu, name="menu"),
    path('about/', views.about, name='about'),
    path('menu_by_id', views.menu_by_id, name="menu by id")
]