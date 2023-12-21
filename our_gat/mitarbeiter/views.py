from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory #a way to create multiple forms inside one form

from .models import *
from .forms import OrderForm

from .filters import OrderFilter

# Create your views here.

def home(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()

    total_customers = customers.count()
    total_orders = orders.count()

    delivered = orders.filter(status='Delivered').count()
    pending = orders.filter(status='Pending').count()


    context = {'orders' : orders, 'customers' : customers, 'total_orders': total_orders, 'delivered': delivered, 'pending': pending}

    return render(request, 'mitarbeiter/dashboard.html', context )

def mitarbeiter(request, pk):
    customer = Customer.objects.get(id=pk)

    orders = customer.order_set.all()
    order_count = orders.count()
        #Filter-Ablauf: the data gets rendered in "queryset=orders", thrown into the filter with "request.GET" --> then we remake this filtered data from "orders" into an new queryset with "orders = myFilter.qs"
    myFilter = OrderFilter(request.GET, queryset=orders)
    orders = myFilter.qs

    context = {
        'customer': customer,
        'orders': orders,
        'order_count': order_count,
        'myFilter': myFilter,
    }
    return render(request, 'mitarbeiter/mitarbeiter.html', context)



def ziele(request):
    products = Product.objects.all()

    return render(request, 'mitarbeiter/ziele.html', {'products': products})


def createOrder(request, pk):
    OrderFormSet = inlineformset_factory(Customer, Order, fields=('product', 'status'), extra=10) #here we create the instance of the formset--inlineformset_factory(Parentobject, Childobject, the fields that we want to be shown) --> Order is referenced to Customer, and we have multiple orders
                                                                                              # extra=10 gibt die Anzahl der Forms an, die auf Seite angezeigt werden sollen. Also 10   
    customer = Customer.objects.get(id=pk) #now we can get the customer by the id und pass in the pk from the argument
    
    formset = OrderFormSet(queryset=Order.objects.none(), instance=customer)
    #  form = OrderForm(initial={'customer': customer}) #um den Namen des Customers im ersten Feld vorausgefüllt zu haben

    
    if request.method == 'POST':
        #print('Printing POST: ', request.POST) 
        #form = OrderForm(request.POST)
        formset = OrderFormSet(request.POST, instance=customer)
        if formset.is_valid():
            formset.save()
            return redirect('/')
   
    context = {'formset': formset}
    return render(request, 'mitarbeiter/order_form.html', context)

def updateOrder(request, pk):

#um die form mit der Person und seinen hinterlegten Daten vorauszufüllen; außerdem noch bei OrderForm()-->"instance=order" in Klammer setzen
    order = Order.objects.get(id=pk)

    form = OrderForm(instance=order)
    if request.method == 'POST':
            #print('Printing POST: ', request.POST) -->nur als Test gemacht
            form = OrderForm(request.POST, instance=order) #auch hier "instance=order" hinzufügen, um neue Veränderungen zu speichern in der gleichen Instanz, um keine neue zu erstellen!
            if form.is_valid():
                form.save()
                return redirect('/')

    context = {'form': form}
    return render(request, 'mitarbeiter/order_form.html', context)

def deleteOrder(request, pk):
    order = Order.objects.get(id=pk)
    if request.method == 'POST':
        order.delete()
        return redirect('/')
    
    context= {'item': order}        #wird in delete.html über {{item}} eingefügt unser Item ist also der Bestellte Objekt

    return render(request, 'mitarbeiter/delete.html', context)
