from django.urls import path 
from . import views

urlpatterns = [
    path('book/', views.book_form, name='book form')
]