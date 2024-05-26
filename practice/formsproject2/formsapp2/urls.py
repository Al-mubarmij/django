from . import views 
from django.urls import path 

urlpatterns = [
    path('signup', views.signup, name="singup"),
    path('signupdata', views.userdata, name='userdata'),
]