from django.shortcuts import render, HttpResponseRedirect
from django.views.generic import TemplateView, CreateView
from django.contrib.auth.views import (
    LoginView, 
    LogoutView as Logout
)
from django.contrib.auth import login, authenticate

from auth.forms import artistForm, userForm
from main import models

# Create your views here.

class Login(TemplateView, LoginView):
    template_name = 'auth/HomePage.html'
    # redirect_authenticated_user = True

class ArtistSignUp(TemplateView):
    template_name = 'auth/ArtistSignUp.html'

    def get(self, request):
        userCreationForm = userForm()
        artistCreationForm = artistForm()

        forms = {
            'userForm': userCreationForm,
            'artistForm': artistCreationForm
        }

        return render(request, self.template_name, forms)

    def post(self, request):
        user = userForm(request.POST)
        artist = artistForm(request.POST)

        if user.is_valid and artist.is_valid():
            artistObject = artist.save(commit = False)
            userObject = user.save(commit = False)
            artistObject.save()
            userObject.artist =  artistObject
            userObject.save()

            return HttpResponseRedirect('/paintings')
        else:
            userCreationForm = userForm()
            artistCreationForm = artistForm()

            forms = {
                'userForm': userCreationForm,
                'artistForm': artistCreationForm
            }

            return render(request, self.template_name, forms)

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

    def form_valid(request, form):
        newUser = form.save(commit = False)
        newUser.is_staff = True
        newUser.save()
        return HttpResponseRedirect('/paintings')

