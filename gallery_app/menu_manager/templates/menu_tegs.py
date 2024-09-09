from django import template
from django.urls import resolve, reverse

from gallery_app.menu_manager.models import Menu

register = template.Library()


@register.simple_tag
def draw_menu(menu_name):
    menu = Menu.objects.get(name=menu_name)
    return draw_menu_items(menu)


def draw_menu_items(menu, parent=None, level=0):
    items = menu.items.filter(parent_menu=parent).order_by('name')
    output = ''
    for item in items:
        is_active = (item.url == resolve(request.path).url_name)
        output += f'<li class="{is_active and "active" or ""}">'
        if item.url:
            output += f'<a href="{item.url}">{item.name}</a>'
        else:
            output += f'<span>{item.name}</span>'
        if item.items.exists():
            output += f'<ul class="{is_active and "active" or ""}">{draw_menu_items(menu, item, level+1)}</ul>'
        output += '</li>'
    return output
