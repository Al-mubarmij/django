from django.urls import path 
from . import views 

urlpatterns = [
    path('travel/', views.book_flight, name="book flight"),
]