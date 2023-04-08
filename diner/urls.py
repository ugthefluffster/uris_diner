from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name="main"),
    path('dishes/', views.all_dishes, name="all_dishes"),
    path('dishes/<int:category_id>', views.category_dishes, name="category_dishes"),
    path('cart/', views.show_cart, name="show_cart"),
    path('cart/add/', views.add_to_cart, name="add_to_cart"),
    path('cart/change/', views.change_cart_item, name="change_cart_item"),
    path('cart/delete/', views.delete_cart_item, name="delete_cart_item"),
    path('order/', views.fill_order, name="fill_order"),
    path('delivery/', views.show_delivery, name="show_delivery")
]