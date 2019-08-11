from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from django.contrib.auth.views import LoginView
# Create your views here.

from main import models

class Index(ListView):
    model = models.Painting
    template_name = 'main/index.html'

class Profile(DetailView):
    model = models.Profile
    template_name = 'main/user-profile.html'

class Artists(ListView):
    model = models.Artist
    template_name = 'main/artists.html'