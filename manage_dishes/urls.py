from django.urls import path
from . import views 

urlpatterns = [
    path('', views.show_dishes, name="show_dishes"),
    path('add/', views.add_dish, name="show_dish"),
    path('edit/', views.edit_dish, name="show_dish"),
    path('delete/', views.delete_dish, name="show_dish")
]