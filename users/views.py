from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout, update_session_auth_hash
from django.contrib import messages
from main.models import *
from main.forms import *

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
            messages.info(request, f"User '{new_user.username}' created! You can now place orders.")
            return redirect('all_dishes')
    return render(request, 'users/signup.html', {'form':form})

def user_login(request):
    if request.user.is_authenticated:
        return redirect('all_dishes')
    form = CustomAuthenticationForm()
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if request.POST['next']:
                return redirect(request.POST['next'])
            return redirect('all_dishes')
    return render(request, 'users/login.html', {'form':form})

@login_required(login_url='user_login')
def user_logout(request):
    logout(request)
    return redirect('main')

@login_required(login_url='user_login')
def show_user_info(request):
    return render(request, 'users/info.html')

@login_required(login_url='user_login')
def change_user_info(request):
    user = request.user
    form = ChangeInfoForm(instance=user)
    if request.method=='POST':
        form=ChangeInfoForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.info(request, f"Your information have been saved.")
            return redirect('show_user_info')
    return render(request, 'users/change_info.html', {'form':form})

@login_required(login_url='user_login')
def change_user_password(request):
    user = request.user
    form = CustomPasswordChangeForm(user)
    if request.method=='POST':
        form = CustomPasswordChangeForm(user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.info(request, f"Password changed successfully.")
            return redirect('show_user_info')
    return render(request, 'users/change_password.html', {'form':form})

@login_required(login_url='user_login')
def user_history(request):
    past_orders = sorted(request.user.cart_set.filter(delivery__is_delivered=True), key=lambda order: order.delivery.created, reverse=True) 
    return render(request, 'users/history.html', {'past_orders':past_orders})