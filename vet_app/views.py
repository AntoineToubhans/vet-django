from django.conf import settings
from django.shortcuts import render


from .models import People
from .models import Service


def index(request):
    return render(request, 'home.html', {
        'current_page': 'home',
    })


def contact(request):
    return render(request, 'contact.html', {
        'current_page': 'contact',
    })


def news(request):
    return render(request, 'news.html', {
        'current_page': 'news',
    })


def team(request):
    people = People.objects.get_ordered_people()

    return render(request, 'team.html', {
        'current_page': 'team',
        'people': people,
    })


def service(request, service_id):
    service = Service.objects.get(id=service_id)

    return render(request, 'service.html', {
        'current_page': 'home',
        'current_service': service,
    })
