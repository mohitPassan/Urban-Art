from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, CreateView
from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect
# Create your views here.

from main import models

class Index(ListView, LoginView):
    model = models.Painting
    template_name = 'main/index.html'

class Profile(DetailView):
    model = models.Artist
    template_name = 'main/user-profile.html'

class Artists(ListView):
    model = models.Artist
    template_name = 'main/artists.html'

class AddPainting(CreateView):
    model = models.Painting
    fields = [
        'name',
        'price',
        'medium',
        'style',
        'size',
        'photo'
    ]
    template_name = 'main/add-painting.html'

    def get_success_url(self):
        return '/index/profile/{}'.format(self.kwargs['artist_id'])

    def form_valid(self, form):
        artist = models.Artist.objects.get(id = self.kwargs['artist_id'])

        newPainting = form.save(commit=False)
        newPainting.artist = artist
        newPainting.save()

        return HttpResponseRedirect(self.get_success_url())
