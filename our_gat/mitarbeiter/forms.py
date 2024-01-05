from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


from .models import Order



class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = '__all__'

        #Wenn man nicht alle Felder des Models sehen möchte --> fields = ['customer', 'product']

class CreateUserForm(UserCreationForm): #customizing the UserCreationForm, Erweiterung um ein email-Feld und Passwort-Feld
    class Meta:
        model = User
        fields = ['username', 'email', 'password2']
