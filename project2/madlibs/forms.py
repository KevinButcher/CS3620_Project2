from django import forms
from .models import MadLib

class MadLibForm(forms.Form):
    noun = forms.CharField(label='Noun', max_length=100)
    verb = forms.CharField(label='Verb (ending in "ing")', max_length=100)
    adjective = forms.CharField(label='Adjective', max_length=100)
    place = forms.CharField(label='Place', max_length=100)
    name = forms.CharField(label="Person's Name", max_length=100)
    color = forms.CharField(label='Color', max_length=100)
    noun2 = forms.CharField(label='Plural Noun', max_length=100)
