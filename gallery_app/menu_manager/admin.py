from django.contrib import admin

from .models import Menu, MenuItem


class MenuAdmin(admin.ModelAdmin):
    fields = ('name',)
    list_display = ('name',)


class MenuItemAdmin(admin.ModelAdmin):
    fields = ('name',)
    list_display = ('name',)


admin.site.register(Menu, MenuAdmin)
admin.site.register(MenuItem, MenuItemAdmin)
