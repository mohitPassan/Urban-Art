from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.contrib.auth.views import LoginView
# Create your views here.

from main import models

class Index(ListView):
    model = models.Painting
    template_name = 'main/index.html'