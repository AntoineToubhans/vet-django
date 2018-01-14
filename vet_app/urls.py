from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('team/', views.team, name='team'),
    path('404/', views.not_found, name='not_found'),
]

handler404 = 'vet_app.views.not_found'
