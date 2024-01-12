from django.shortcuts import render, redirect, get_object_or_404

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import CreateUserForm, UserAuthenticationForm, EventForm

from .models import Event
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json


# Create your views here.

def registerPage2(request):
    form = CreateUserForm()
    
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user)
            return redirect('login2')
        
    context = {'form': form}
    return render(request, 'kalender/register2.html', context)

def loginPage2(request):

    if request.method =='POST':
        username = request.POST.get('username') #username und password werden vom Input aus login.html genommen
        password =  request.POST.get('password')

        user = authenticate(request, username=username, password = password)
    
        if user is not None:
           login(request, user)
           return redirect('home2')
        else: 
            messages.info(request,'Username OR password is incorrect')

    context = {}
    return render(request, 'kalender/login2.html', context)

def logoutUser2(request):
    logout(request)
    return redirect('login2')

@login_required(login_url='login2') #Decorator, um User erlauben auf Seite zuzugreifen, wenn er denn eingeloggt ist. ansonsten wird er wieder auf Login-Seite zurückgeleitet
def home2(request):
    context = {}
    return render(request, 'kalender/home2.html', context )


def event_list(request):
    events = Event.objects.all()
    return render(request, 'kalender/event_list.html', {'events': events})

def add_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('event_list')
    else:
        form = EventForm()
    return render(request, 'kalender/add_event.html', {'form': form})







def get_events(request):
    events = Event.objects.all()
    serialized_events = []
    for event in events:
        serialized_events.append({
            'id': event.id,
            'title': event.title,
            'start': event.start_date.strftime('%Y-%m-%dT%H:%M:%S'),
            'end': event.end_date.strftime('%Y-%m-%dT%H:%M:%S'),
        })
    return JsonResponse(serialized_events, safe=False)






@csrf_exempt
def update_event(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        event_id = data.get('id')
        updated_title = data.get('title')
        updated_start_date = data.get('start')
        # Get other updated fields

        # Retrieve the event from the database
        event = Event.objects.get(id=event_id)
        event.title = updated_title
        event.start_date = updated_start_date
        # Update other fields
        event.save()

        return JsonResponse({'message': 'Event updated successfully'})
    else:
        return JsonResponse({'error': 'Invalid request method'})



def delete_data(request, pk):
    # Retrieve the instance of YourModel based on the provided primary key (pk)
    event = get_object_or_404(Event, pk=pk)

    # Perform deletion
    event.delete()

    # Return a JSON response indicating successful deletion
    return JsonResponse({'message': 'Event deleted successfully'}, status=200)