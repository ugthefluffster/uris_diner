from django.urls import path
from . import views 

urlpatterns = [
    path('login/', views.backoffice_login, name="backoffice_login"),
    path('logout/', views.backoffice_logout, name="backoffice_logout"),
    path('deliveries/', views.manage_deliveries, name="manage_deliveries"),
    path('categories/', views.show_categories, name="show_categories"),
    path('categories/add', views.add_category, name="show_category"),
    path('categories/edit', views.edit_category, name="show_category"),
    path('categories/delete', views.delete_category, name="show_category"),
    path('dishes/', views.show_dishes, name="show_dishes"),
    path('dishes/add', views.add_dish, name="show_dish"),
    path('dishes/edit', views.edit_dish, name="show_dish"),
    path('dishes/delete', views.delete_dish, name="show_dish")
]