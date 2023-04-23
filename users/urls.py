from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.user_signup, name="user_signup"),
    path('login/', views.user_login, name="user_login"),
    path('logout/', views.user_logout, name="user_logout"),
    path('info/', views.show_user_info, name="show_user_info"),
    path('info/change/', views.change_user_info, name="change_user_info"),
    path('info/change/password/', views.change_user_password, name="change_user_password"),
    path("history/", views.user_history, name="user_history")
]