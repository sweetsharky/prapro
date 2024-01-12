from django.urls import path
from . import views

urlpatterns = [
   path('register2/', views.registerPage2, name="register2"),
   path('login2/', views.loginPage2, name="login2"),
   path('logout2/', views.logoutUser2, name="logout2"),
   
   path('home2', views.home2, name="home2"),

   path('event_list/', views.event_list, name="event_list"),
   path('add_event/', views.add_event, name='add_event'),
   path('api/events/', views.get_events, name='get_events'),

   path('delete-data/<int:pk>/', views.delete_data, name='delete_data'),
]