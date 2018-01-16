from django.conf import settings
from django.shortcuts import render


from .models import People


def index(request):
    return render(request, 'home.html', {
        'current_page': 'home',
    })


def team(request):
    people = People.objects.all().filter(is_active=True)

    return render(request, 'team.html', {
        'current_page': 'team',
        'people': people,
    })


def not_found(request):
    return render(request, '404.html', {
        'menu': settings.VET_APP_MENU,
        'current_page': 'not_found',
    })
