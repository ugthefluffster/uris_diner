from django.urls import path
from . import views 

urlpatterns = [
    path('', views.show_dishes, name="show_dishes"),
    path('add/', views.add_dish, name="add_dish"),
    path('edit/<int:id>', views.edit_dish, name="edit_dish"),
    path('delete/<int:id>', views.delete_dish, name="delete_dish")
]