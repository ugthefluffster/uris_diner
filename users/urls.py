from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.user_signup, name="user_signup"),
    path('login/', views.user_login, name="user_login"),
    path('logout/', views.user_logout, name="user_logout"),
    path('info/', views.user_info, name="user_info"),
    path("history/", views.user_history, name="user_history")
]