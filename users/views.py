from django.shortcuts import render, redirect
from diner.models import *
from django.contrib.auth.decorators import login_required

def user_signup(request):
    return render(request, 'users/signup.html')

def user_login(request):
    return render(request, 'users/login.html')

@login_required(login_url='user_login')
def user_info(request):
    return render(request, 'users/info.html')

@login_required(login_url='user_login')
def user_history(request):
    return render(request, 'users/history.html')