from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.book_view, name="booking form"),
]