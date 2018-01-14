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


def not_found(request):
    return render(request, '404.html', {
        'menu': settings.VET_APP_MENU,
        'current_page': 'not_found',
    })
