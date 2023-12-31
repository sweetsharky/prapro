from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.loginPage, name="login"),
    path('register/', views.registerPage, name="register"),

    path('', views.home, name="home"),
    path('ziele/', views.ziele, name='ziele'),
    path('mitarbeiter/<str:pk>', views.mitarbeiter, name='mitarbeiter'),

    path('create_order/<str:pk>', views.createOrder, name="create_order"),
    path('update_order/<str:pk>/', views.updateOrder, name="update_order"),
    path('delete_order/<str:pk>/', views.deleteOrder, name="delete_order"),

]