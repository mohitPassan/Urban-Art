from django.shortcuts import render
from django.views.generic import TemplateView, CreateView
from django.contrib.auth.views import LoginView

from main import models

# Create your views here.

class Login(TemplateView, LoginView):
    template_name = 'auth/HomePage.html'
    # redirect_authenticated_user = True

class ArtistSignUp(CreateView):
    model = models.Profile
    template_name = 'auth/ArtistSignUp.html'
    fields = [  
        'first_name',
        'last_name',
        'username',
        'password',
        'email',
        'contact',
        'address'
    ]

    def form_valid(self, form):
        artistWorkEx = self.request.GET.get('workEx')
        artistStyle = self.request.GET.get('style')
        artistMedium = self.request.GET.get('medium')
        
        userArtist = form.save()
        userArtist.foreignkeytoartist.workEx = artistWorkEx
        userArtist.artist.style = artistStyle
        userArtist.artist.medium = artistMedium

        userArtist.save()

        
    success_url = '/paintings'

class UserSignUp(CreateView):
    model = models.Profile
    template_name = 'auth/UserSignUp.html'
    fields = [  
        'first_name',
        'last_name',
        'username',
        'password',
        'email',
        'contact',
        'address'
    ]

    success_url = '/paintings'