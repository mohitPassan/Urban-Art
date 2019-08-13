from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Artist(models.Model):
    workEx = models.PositiveIntegerField()
    style = models.CharField(max_length = 256)
    medium = models.CharField(max_length = 256)
    photo = models.URLField(null = True, blank = True)
    # ToDo: description in markdown

    def __str__(self):
        return self.profile.username

class Profile(User):
    contact = models.CharField(max_length = 15)
    address = models.TextField()
    artist = models.OneToOneField('Artist', on_delete = models.CASCADE, null = True, blank = True)

class Painting(models.Model):
    name = models.CharField(max_length = 256)
    price = models.IntegerField()
    artist = models.ForeignKey('Artist', on_delete = models.CASCADE)
    medium = models.CharField(max_length = 256)
    style = models.CharField(max_length = 256)
    size = models.CharField(max_length = 256)
    photo = models.URLField(null = True, blank = True)
    soldStatus = models.BooleanField(default = False)

    def __str__(self):
        return self.name

class Payment(models.Model):
    PAYMENT_OPTIONS = [
        ('cc', 'Credit Card'),
        ('dc', 'Debit Card')
    ]
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    painting = models.OneToOneField('Painting', on_delete = models.CASCADE)
    artist = models.ForeignKey('Artist', on_delete = models.CASCADE)
    mode = models.CharField(max_length = 256, choices = PAYMENT_OPTIONS)
    payment_time = models.DateTimeField(auto_now_add=True)
    card_number = models.CharField(max_length = 256)
    name_on_card = models.CharField(max_length = 256)
    expiration_month = models.IntegerField()
    expiration_year = models.IntegerField()
    cvv = models.IntegerField()

    def __str__(self):
        return "{} bought {} from {}".format(self.user.username, self.painting.name, self.artist.profile.username)