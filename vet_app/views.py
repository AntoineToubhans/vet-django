from django.conf import settings
from django.shortcuts import render


def index(request):
    return render(request, 'home.html', {
        'menu': settings.VET_APP_MENU,
    })


def team(request):
    return render(request, 'team.html', {
        'menu': settings.VET_APP_MENU,
    })
