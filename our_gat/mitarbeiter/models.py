from django.db import models

# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name
    

class Tag(models.Model):
    name = models.CharField(max_length=200, null=True)
    
    def __str__(self):
        return self.name

class Product(models.Model):
    CATEGORY = (
    ('Indoor', 'Indoor'),
    ('Out Door', 'Out Door'),
        )

    name = models.CharField(max_length=200, null=True)
    price = models.FloatField(null=True)
    category = models.CharField(max_length=200, null=True, choices=CATEGORY)
    description = models.CharField(max_length=200, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    
    tags = models.ManyToManyField(Tag) #Hier wird die many-to-many relationship mithilfe der tags in das Model Product eingebunden!!!

    def __str__(self):
        return self.name
    

class Order(models.Model):
    STATUS = (
        ('Pending', 'Pending'),
        ('out for delivery', 'Out for delivery'),
        ('Delivered', 'Delivered'),
    )

#hier drunter werden zwei one-to-one Relationships gemacht --> in customer werden die Werte von Customer reingeschrieben! on_delete ist hierbei, dass bei Löschung nicht Parent-model mitgelöscht wird, sondern nur NULL gesetzt werden soll
    #konkret wird damit einer Bestellung(Order) ein Objekt (der Klasse Customer) zugeordnet. D.h. wenn ich eine Bestellung habe, weiß ich auch, wer für diese Bestellung der Customer ist!
    #dann kann ich, wenn customer1 = Peter Piper ist, mit "customer1.order_set.all()" alle Bestellungen bekommen, die Peter Piper gemacht hat
    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL) 
    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL) # in product kommen die Werte von Product rein! Order hat also eine Beziehung zu Product-Instanzen
    
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=200, null=True, choices=STATUS) #choices macht Dropdown menu möglich mit den Werten, die wird in STATUS initialisiert haben

    def __str__(self):
        return self.product.name