from django.shortcuts import render, HttpResponseRedirect
from django.views.generic import TemplateView, DeleteView
from django.contrib.auth.views import (
    LoginView, 
    LogoutView as Logout
)
from django.contrib.auth import login, authenticate
from django.urls import reverse_lazy

from auth.forms import artistForm, userForm
from main import models

# Create your views here.

class Login(LoginView):
    template_name = 'auth/HomePage.html'
    redirect_authenticated_user = True

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
        artist = artistForm(request.POST, request.FILES)

        if user.is_valid() and artist.is_valid():
            artistObject = artist.save(commit = False)
            userObject = user.save(commit = False)

            if not artistObject.photo:
                artistObject.photo = 'profile_image/default-user-icon-28.jpg'
            
            artistObject.save()
            userObject.artist =  artistObject
            userObject.save()

            userObject = authenticate(username=user.cleaned_data['username'], password=user.cleaned_data['password1'])
            login(request, userObject)

            return HttpResponseRedirect('/')
        else:
            userCreationForm = userForm()
            artistCreationForm = artistForm()

            forms = {
                'userForm': userCreationForm,
                'artistForm': artistCreationForm
            }

            return render(request, self.template_name, forms)

class UserSignUp(TemplateView):
    template_name = 'auth/UserSignUp.html'

    def get(self, request):
        userCreationForm = userForm()

        form = {
            'userForm': userCreationForm
        }

        return render(request, self.template_name, form)

    def post(self, request):
        user = userForm(request.POST)

        if user.is_valid():
            user.save()
            user = authenticate(username=user.cleaned_data['username'], password=user.cleaned_data['password1'])
            login(request, user)
            return HttpResponseRedirect('/')
        else:
            userCreationForm = userForm()
            form = {
                'userForm': userCreationForm
            }
            return render(request, self.template_name, form)

class DeleteUser(DeleteView):
    model = models.Profile
    template_name = 'auth/delete-user.html'
    success_url = reverse_lazy('home-page')

class DeleteArtist(DeleteView):
    model = models.Artist
    template_name = 'auth/delete-artist.html'
    success_url = reverse_lazy('home-page')

