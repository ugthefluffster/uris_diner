from django.urls import path, include
from . import views 

urlpatterns = [
    path('login/', views.backoffice_login, name="backoffice_login"),
    path('orders/', views.manage_orders, name="manage_orders"),
    path('orders/history', views.show_orders_history, name="show_orders_history"),
    path('categories/add/', views.add_category, name="add_category"),
    path('categories/edit/<int:id>', views.edit_category, name="edit_category"),
    path('categories/up/<int:id>', views.category_up, name="category_up"),
    path('categories/down/<int:id>', views.category_down, name="category_down"),
    path('categories/delete/<int:id>', views.delete_category, name="delete_category"),
    path('dishes/add/', views.add_dish, name="add_dish"),
    path('dishes/edit/<int:id>', views.edit_dish, name="edit_dish"),
    path('dishes/delete/<int:id>', views.delete_dish, name="delete_dish")
]