from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'services'
urlpatterns = [
    path('', views.index, name='home'),
    path('prices/', views.show_prices, name='prices'),
    path('contacts/', views.show_contacts, name='contacts'),
    path('cleaning/', views.show_cleaning, name='cleaning'),
]
