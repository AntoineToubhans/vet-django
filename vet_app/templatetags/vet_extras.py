from django import template
from django.conf import settings


register = template.Library()


@register.inclusion_tag('header.html', takes_context=True)
def vet_header(context):
    return {
        'menu': settings.VET_APP_MENU,
        'current_page': context.get('current_page', 'none')
    }
