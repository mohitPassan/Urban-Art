from django import forms
from main import models
from django.contrib.auth.forms import UserCreationForm

class userForm(UserCreationForm):
    email = forms.EmailField(required = True)
    first_name = forms.CharField(max_length = 256)
    last_name = forms.CharField(max_length = 256)

    class Meta:
        model = models.Profile
        fields = [
            'first_name',
            'last_name',
            'username',
            'password1',
            'password2',
            'email',
            'contact',
            'address'
        ]

    def save(self, commit = True):
        user = super().save(commit = False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']

        if commit:
            user.save()
        return user

class artistForm(forms.ModelForm):
    class Meta:
        model = models.Artist
        fields = [
            'workEx',
            'style',
            'medium'
        ]