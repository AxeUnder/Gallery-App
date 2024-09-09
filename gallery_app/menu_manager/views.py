from django.shortcuts import redirect, render

from .models import Menu, MenuItem, MenuForm, MenuItemForm


def menu_list(request):
    """Отображение списка меню."""
    menus = Menu.objects.all()
    return render(request, 'menu.html', {'menus': menus})


def delete_menu_item(request, pk):
    """Удаление элемента меню."""
    item = MenuItem.objects.get(pk=pk)
    item.delete()
    return redirect('menu_list')


def get_menu_item(request, pk):
    """"Получение элемента меню."""
    menu = Menu.objects.get(pk=pk)
    return render(request, 'menu.html', {'menu': menu})


def add_menu(request):
    """Добавление меню."""
    if request.method == 'POST':
        form = MenuForm(request.POST)
        if form.is_valid():
            new_menu = form.save()
            return redirect('menu_list', pk=new_menu.id)

    else:
        form = MenuForm()

    return render(request, 'add_menu.html', {'form': form})


def add_menu_item(request):
    """Добавление элемента меню."""
    if request.method == 'POST':
        form = MenuItemForm(request.POST)
        if form.is_valid():
            parent_menu_id = request.POST.get('parent_menu_id', -1)
            new_menu_item = form.save(parent_menu_id=parent_menu_id)
            return redirect('menu_list')
    else:
        parent_menu_id = request.GET.get('parent_menu')
        parent_menu = Menu.objects.get(pk=parent_menu_id)
        items = MenuItem.objects.filter(parent_menu=parent_menu)

        for item in items:
            form = MenuItemForm(initial={'name': item.name, 'url': item.url})
            form.parent_menu_ = parent_menu
            form.save()
