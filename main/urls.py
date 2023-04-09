from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name="main"),
    path('dishes/', views.all_dishes, name="all_dishes"),
    path('dishes/<int:category_id>', views.category_dishes, name="category_dishes"),
    path('order/', views.fill_order, name="fill_order"),
    path('delivery/', views.show_delivery, name="show_delivery")
]