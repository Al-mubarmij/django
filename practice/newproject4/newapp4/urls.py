from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home),
    path('getuser/<name>/<int:id>', views.pathview, name='pathview'),
    path('getuser/', views.qryview, name='qryview'),
    '''path('showform/', views.showform, name="showform"),'''
]