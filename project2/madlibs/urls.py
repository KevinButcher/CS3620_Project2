from django.urls import path
from . import views

app_name = 'madlibs'
urlpatterns = [
    # /madlibs
    path('', views.index, name="index"),
    # /madlibs/1 /madlibs/2
    path('madlib/', views.madlibForm, name='madlib-form')
]