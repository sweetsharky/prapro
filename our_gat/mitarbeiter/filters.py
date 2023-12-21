import django_filters

from .models import *

#here we create our filters
class OrderFilter(django_filters.FilterSet):
    class Meta:
        model = Order
        fields = '__all__'
        exclude = [ 'customer', 'date_created']