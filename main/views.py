from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User

# Create your views here.

from main import models

class Index(ListView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        allArtists = models.Artist.objects.all()
        context['artists'] = allArtists
        return context

    model = models.Painting
    template_name = 'main/index.html'

class ChangeProfilePicture(UpdateView):
    model = models.Artist
    fields = ['photo']
    template_name = 'main/change-profile.html'
    
    def get_success_url(self):
        return '/index/current-user/'

    def form_valid(self, form):
        form.save()

        return HttpResponseRedirect(self.get_success_url())

class ArtistProfile(DetailView):
    model = models.Artist
    template_name = 'main/artist-profile.html'

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
        return '/index/current-user'

    def form_valid(self, form):
        artist = models.Artist.objects.get(id = self.kwargs['artist_id'])

        newPainting = form.save(commit=False)
        newPainting.artist = artist
        newPainting.save()

        return HttpResponseRedirect(self.get_success_url())

class Painting(DetailView):
    model = models.Painting
    template_name = 'main/painting.html'

class Payment(CreateView):
    template_name = 'main/payment.html'
    model = models.Payment

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['artist'] = models.Artist.objects.get(id = self.kwargs['artist_id'])
        context['painting'] = models.Painting.objects.get(id = self.kwargs['painting_id'])
        return context

    fields = [
        'mode',
        'card_number',
        'name_on_card',
        'expiration_month',
        'expiration_year',
        'cvv'
    ]

    def form_valid(self, form):
        artist = models.Artist.objects.get(id = self.kwargs['artist_id'])
        user = User.objects.get(id = self.kwargs['user_id'])
        painting = models.Painting.objects.get(id = self.kwargs['painting_id'])
        painting.soldStatus = True
        painting.save()
        paymentDetails = form.save(commit = False)

        paymentDetails.user = user
        paymentDetails.artist = artist
        paymentDetails.painting = painting

        paymentDetails.save()

        return HttpResponseRedirect('/index/thankyou')

class Success(TemplateView):
    template_name = 'main/success.html'

def CurrentProfile(request):
    try:
        user = models.Artist.objects.get(profile = request.user)
    except:
        user = models.Profile.objects.get(id = request.user.id)

    try:
        buyers = models.Payment.objects.filter(artist = models.Artist.objects.get(profile = request.user))
    except:
        buyers = None

    Context = {
        'user': user,
        'orders': models.Payment.objects.filter(user = request.user),
        'buyers': buyers
    }

    return render(request, 'main/current-user.html', Context)