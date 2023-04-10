from django.urls import path, include
from . import views 

urlpatterns = [
    path('login/', views.backoffice_login, name="backoffice_login"),
    path('logout/', views.backoffice_logout, name="backoffice_logout"),
    path('orders/', views.manage_orders, name="manage_orders"),
    path('orders/history', views.show_orders_history, name="show_orders_history"),
    path('categories/', include('manage_categories.urls')),
    path('dishes/', include('manage_dishes.urls'))
]