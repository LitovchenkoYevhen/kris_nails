from django.shortcuts import render, get_object_or_404, redirect
from .models import Services, Cleaning, Nails


def index(request):
    photos_list = Nails.objects.all()
    context = {'photos_list': photos_list}
    return render(request, 'services/index.html', context)

def show_prices(request):
    services = Services.objects.order_by('-price')
    context = {'service_list': services}
    return render(request, 'services/prices.html', context)

def show_contacts(request):
    return render(request, 'services/contacts.html')

def show_cleaning(request):
    cleaning_list = Cleaning.objects.all()
    context = {'cleaning_list': cleaning_list}
    return render(request, 'services/cleaning_list.html', context)

