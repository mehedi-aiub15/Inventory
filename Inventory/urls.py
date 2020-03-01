from django.contrib import admin
from django.urls import path,include

from inventory_app import views

urlpatterns = [
    path('admin/',admin.site.urls),
    path('',views.index, name='index'),
    path('items_list/',views.items_list, name='items_list'),
    path('item/<int:pk>/',views.item_detail, name='item_detail'),
    path('items_pagination/',views.items_pagination, name='items_pagination'),
    path('api/v1/items/',views.item_collection, name='item_collection'),
    path('api/v1/items/<int:pk>/',views.item_element, name='item_element'),
]