from django import forms
from main import models

class userForm(forms.ModelForm):
    class Meta:
        model = models.Profile
        fields = [
            'first_name',
            'last_name',
            'username',
            'password',
            'email',
            'contact',
            'address'
        ]

class artistForm(forms.ModelForm):
    class Meta:
        model = models.Artist
        fields = [
            'workEx',
            'style',
            'medium'
        ]