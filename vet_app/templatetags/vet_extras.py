from django import template
from django.conf import settings
from vet_app.models import Service


register = template.Library()


@register.inclusion_tag('header.html', takes_context=True)
def vet_header(context):
    return {
        'menu': settings.VET_APP_MENU,
        'current_page': context.get('current_page', 'none'),
    }


@register.inclusion_tag('services_menu.html', takes_context=True)
def service_menu(context):
    current_service = context.get('current_service')

    return {
        'services': Service.objects.get_services(),
        'selected_service_id': current_service.id if current_service else None,
    }


@register.inclusion_tag('pagination.html')
def pagination(object_list, paginator):
    return {
        'object_list': object_list,
        'page_range': paginator.page_range,
    }
