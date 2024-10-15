from django.shortcuts import render, get_object_or_404, redirect
from .models import MadLib
from .forms import MadLibForm
import random
# add this in if necessary
# from django.contrib.auth.decorators import login_required
# from django.contrib import messages


# Create your views here.

def index(request):
    return render(request, 'madlibs/index.html', {"intro": "Welcome to my madlib project!"})

def madlibForm(request):
    if request.method == 'POST':
        form = MadLibForm(request.POST)
        if form.is_valid():
            story = random.choice(MadLib.objects.all())
            # **form.cleaned_data:
            # the ** syntax passes the form information (key-value pair) into placeholders within the madlib
            madlib = madlib.template.format(**form.cleaned_data_)
            return render(request, 'story.html', {'madlib': madlib, 'title': story.title})
    else:
        form = MadLibForm()
    return render(request, 'madlibs/madlib-form.html', {'form': form})

# Create Frontend using Django (Create a User-Friendly Design)

# Use Views/Templates/URL Patterns as You See Best Fit
# Use Database as You See Best Fit
# Display Story to The User After Submission
# Minimums
#   A Minimum of 7 Form Fields (For example place, adjective, famous person)
#   A Minimum of 15 Random Mad Lib Stories
#       use {} with the key value inside to replace with form information