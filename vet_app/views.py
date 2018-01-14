from django.shortcuts import render


def index(request):
    return render(request, 'home.html', {})


def team(request):
    return render(request, 'team.html', {})
