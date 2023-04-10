from django.urls import path
from . import views 

urlpatterns = [
    path('', views.show_categories, name="show_categories"),
    path('add/', views.add_category, name="show_category"),
    path('edit/', views.edit_category, name="show_category"),
    path('delete/', views.delete_category, name="show_category"),
]