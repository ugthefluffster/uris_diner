from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout, update_session_auth_hash
from main.models import *
from .forms import *

def user_signup(request):
    if request.user.is_authenticated:
        return redirect('all_dishes')
    form = CustomUserCreationForm()
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            new_user = authenticate(request, 
                username = request.POST['username'],
                password = request.POST['password1'])
            new_user_cart = Cart(user = new_user)
            new_user_cart.save()
            login(request, new_user)
            return redirect('all_dishes')
    return render(request, 'users/signup.html', {'form':form})

def user_login(request):
    # why shouldn't staff be able to log in through here?
    if request.user.is_authenticated:
        return redirect('all_dishes')
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('all_dishes')
    return render(request, 'users/login.html', {'form':form})

def user_logout(request):
    logout(request)
    return redirect('main')

@login_required(login_url='user_login')
def show_user_info(request):
    return render(request, 'users/info.html')

@login_required(login_url='user_login')
def change_user_info(request):
    user = request.user
    form = ChangeInfoForm(
        instance=user,
        data={
            "email":user.email, 
            "first_name":user.first_name, 
            "last_name":user.last_name})
    if request.method=='POST':
        form=ChangeInfoForm(instance=user, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('show_user_info')
    return render(request, 'users/change_info.html', {'form':form})

@login_required(login_url='user_login')
def change_user_password(request):
    user = request.user
    form = PasswordChangeForm(user)
    if request.method=='POST':
        form = PasswordChangeForm(user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('show_user_info')
    return render(request, 'users/change_password.html', {'form':form})

@login_required(login_url='user_login')
def user_history(request):
    return render(request, 'users/history.html')