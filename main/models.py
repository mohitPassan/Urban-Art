from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Artist(models.Model):
    workEx = models.PositiveIntegerField()
    style = models.CharField(max_length = 256)
    medium = models.CharField(max_length = 256)
    photo = models.URLField(null = True, blank = True)
    # ToDo: description in markdown

class Profile(User):
    contact = models.CharField(max_length = 15)
    address = models.TextField()
    artist = models.OneToOneField('Artist', on_delete = models.CASCADE)

class Painting(models.Model):
    name = models.CharField(max_length = 256)
    price = models.IntegerField()
    artist = models.ForeignKey('Artist', on_delete = models.CASCADE)
    medium = models.CharField(max_length = 256)
    style = models.CharField(max_length = 256)
    size = models.CharField(max_length = 256)

class Payment(models.Model):
    PAYMENT_OPTIONS = [
        ('cc', 'Credit Card'),
        ('dc', 'Debit Card'),
        ('net', 'Net Banking'),
        ('cash', 'Cash'),
        ('upi', 'UPI')
    ]
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    painting = models.OneToOneField('Painting', on_delete = models.CASCADE)
    artist = models.ForeignKey('Artist', on_delete = models.CASCADE)
    mode = models.CharField(max_length = 256, choices = PAYMENT_OPTIONS)
    payment_time = models.DateTimeField(auto_now_add=True)