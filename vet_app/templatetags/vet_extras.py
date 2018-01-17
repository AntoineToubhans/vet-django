from django import template
from django.conf import settings
from vet_app.models import Service


register = template.Library()


@register.inclusion_tag('header.html', takes_context=True)
def vet_header(context):
    return {
        'menu': settings.VET_APP_MENU,
        'current_page': context.get('current_page', 'none')
    }


@register.inclusion_tag('services_menu.html')
def service_menu():
    return {
        'services': Service.objects.get_services()
    }
