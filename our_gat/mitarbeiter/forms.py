from django.forms import ModelForm
from .models import Order

class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = '__all__'

        #Wenn man nicht alle Felder des Models sehen möchte --> fields = ['customer', 'product']