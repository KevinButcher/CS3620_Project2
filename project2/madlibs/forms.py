from django import forms
from .models import MadLib

class MadLibForm(forms.Form):
    # These are placeholders until I figure out what I want to do (need 7 entries for stories)
    place = forms.CharField(label='Place', max_length=100)
