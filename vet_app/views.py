from django.conf import settings
from django.shortcuts import render


def index(request):
    return render(request, 'home.html', {
        'menu': settings.VET_APP_MENU,
        'current_page': 'home',
    })


def team(request):
    return render(request, 'team.html', {
        'menu': settings.VET_APP_MENU,
        'current_page': 'team',
    })
