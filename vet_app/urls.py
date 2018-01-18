from django.urls import path

from . import views

app_name = 'vet_app'
urlpatterns = [
    path('', views.index, name='index'),
    path('team/', views.team, name='team'),
    path('services/<int:service_id>', views.service, name='services'),
]
