from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_cart, name="show_cart"),
    path('add/', views.add_to_cart, name="add_to_cart"),
    path('change/', views.change_cart_item, name="change_cart_item"),
    path('delete/', views.delete_cart_item, name="delete_cart_item")
]