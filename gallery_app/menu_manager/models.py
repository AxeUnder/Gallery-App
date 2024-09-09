from django import forms
from django.db import models
from django.shortcuts import render, redirect


class Menu(models.Model):
    """Модель меню"""
    name = models.CharField(max_length=150)
    parent_menu = models.ForeignKey('Menu', on_delete=models.CASCADE, blank=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['name', 'parent_menu_id'],
                name='unique_name_parent_menu_id'
            )
        ]

    def __str__(self):
        return self.name


class MenuItem(models.Model):
    """Модель элемента меню"""
    name = models.CharField(max_length=150)
    parent_menu = models.ForeignKey('Menu', on_delete=models.CASCADE, blank=True)

    def __str__(self):
        return self.name


class MenuManagerMenu(models.Model):
    name = models.CharField(max_length=255)
    url = models.URLField()
    parent_menu_id = models.IntegerField(default=-1)


class MenuForm(forms.ModelForm):
    """Модель формы создания меню"""
    class Meta:
        model = Menu
        fields = '__all__'
        widgets = {
            'parent_menu_id': forms.IntegerField(
                required=False,
                help_text='Select a menu from the list or enter its ID.'
            )
        }


class MenuItemForm(forms.ModelForm):
    parent_menu_id = forms.IntegerField()


def add_view(request):
    if request.method == 'POST':
        form = MenuForm(request.POST)
        if form.is_valid():
            new_menu = form.save(commit=True)
            return redirect('menu_list')
    else:
        form = MenuForm()
    return render(request, 'add_menu.html', {'form': form})
