from django.urls import path, include
from .views import menu_list, add_menu_item, delete_menu_item, get_menu_item, add_menu


app_name = 'menu_manager'

urlpatterns = [
    path('', menu_list),
    path('menu/', include('menu_manager.urls')),
    path('menu/<int:pk>/', get_menu_item),
    path('add_menu/', add_menu),
    path('add/<int:pk>', add_menu_item),
    path('delete/<int:pk>/', delete_menu_item),
]
