from django.contrib import admin

# Register your models here.

from .models import * #mit dem * sagen wir ,das er ALLE unsere models importieren soll. Sonst müssten wir immer einzeln hinzugügen -->Customer, Product usw...

admin.site.register(Customer)
admin.site.register(Tag)
admin.site.register(Product)
admin.site.register(Order)