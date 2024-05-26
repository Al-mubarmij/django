from django import forms 

class Signup(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    
