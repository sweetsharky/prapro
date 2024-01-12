from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django import forms

from .models import Event



class CreateUserForm(UserCreationForm): #customizing the UserCreationForm, Erweiterung um ein email-Feld und Passwort-Feld
    class Meta:
        model = User
        fields = ['username', 'email', 'password2']


class UserAuthenticationForm(forms.ModelForm): #damit kann in view User Zugriff auf einzelne Module erlaubt/abgelehnt werden

    class Meta:
        model = User
        fields = ['username', 'password']

    def clean(self):
        if self.is_valid():
            username = self.cleaned_data['username']
            password = self.cleaned_data['password']

            if not authenticate(username=username, password=password):
                raise forms.ValidationError('Username oder Passwort sind falsch.')
            


class EventForm(forms.ModelForm):
   
    class Meta:
        model = Event
        fields = ['title', 'start_date', 'end_date']
