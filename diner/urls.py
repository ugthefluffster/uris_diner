from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name="main"),
    path('dishes/', views.all_dishes, name="all_dishes"),
    path('dishes/<int:category_id>', views.category_dishes, name="category_dishes"),
    path('cart/<int:cart_id>', views.show_cart, name="show_cart"),
    path('order/<int:cart_id>', views.fill_order, name="fill_order"),
    path('delivery/<int:order_id>', views.show_delivery, name="show_delivery")
]