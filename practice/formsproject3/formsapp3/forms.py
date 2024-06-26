from django import forms 

from .models import Logger

class LogForm(forms.ModelForm):
    class Meta:
        model = Logger
        fields = '__all__'





# Remove the SHIFTS
'''
SHIFTS = (
    ("1", "Morning"),
    ("2", "Afternoon"),
    ("3", "Evening"),
)
'''

# moved to models.py
'''
class InputForm(forms.Form):
    first_name = forms.CharField(max_length=200)
    last_name = forms.CharField(max_length=200)
    shift = forms.ChoiceField(choices=SHIFTS)
    time_log = forms.TimeField()
'''