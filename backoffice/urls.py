from django.urls import path, include
from . import views 

urlpatterns = [
    path('login/', views.backoffice_login, name="backoffice_login"),
    path('logout/', views.backoffice_logout, name="backoffice_logout"),
    path('orders/', views.manage_orders, name="manage_orders"),
    path('orders/history', views.show_orders_history, name="show_orders_history"),
    path('categories/add/', views.add_category, name="add_category"),
    path('categories/edit/<int:id>', views.edit_category, name="edit_category"),
    path('categories/delete/<int:id>', views.delete_category, name="delete_category"),
    path('dishes/add/', views.add_dish, name="add_dish"),
    path('dishes/edit/<int:id>', views.edit_dish, name="edit_dish"),
    path('dishes/delete/<int:id>', views.delete_dish, name="delete_dish")
]