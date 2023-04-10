from django.urls import path, include
from . import views 

urlpatterns = [
    path('login/', views.backoffice_login, name="backoffice_login"),
    path('logout/', views.backoffice_logout, name="backoffice_logout"),
    path('deliveries/', views.manage_deliveries, name="manage_deliveries"),
    path('categories/', include('manage_categories.urls')),
    path('dishes/', include('manage_dishes.urls'))
]