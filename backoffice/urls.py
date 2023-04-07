from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.backoffice_login, name="backoffice_login"),
    path('deliveries/', views.manage_deliveries, name="manage_deliveries"),
    path('categories/', views.manage_categories, name="manage_categories"),
    path('dishes/', views.manage_dishes, name="manage_dishes")
]