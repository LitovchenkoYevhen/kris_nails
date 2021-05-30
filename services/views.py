from django.shortcuts import render, get_object_or_404, redirect
from .models import Services, Cleaning, Clients, Visits
from django.views.generic import ListView


class HomeServices(ListView):
    model = Visits
    template_name = 'services/home_services_list.html'
    context_object_name = 'photos_list'


def index(request):
    photos_list = Visits.objects.all()
    context = {'photos_list': photos_list}
    return render(request, 'services/index.html', context)


def show_prices(request):
    services = Services.objects.order_by('-price')
    context = {'service_list': services}
    return render(request, 'services/prices.html', context)


def show_contacts(request):
    return render(request, 'services/contacts.html')


def show_cleaning(request):
    header = Cleaning.objects.get(step_name='ЗАГОЛОВОК')
    cleaning_list = Cleaning.objects.all()
    context = {'cleaning_list': cleaning_list, 'header': header}
    return render(request, 'services/cleaning_list.html', context)
