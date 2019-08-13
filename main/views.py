from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, CreateView
from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User

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

class Painting(DetailView):
    model = models.Painting
    template_name = 'main/painting.html'

class Payment(CreateView):
    template_name = 'main/payment.html'
    model = models.Payment
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
    user = models.Artist.objects.get(profile = request.user)

    Context = {
        'artist': user
    }

    return render(request, 'main/current-user.html', Context)