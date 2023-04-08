from django.shortcuts import render, redirect
from diner.models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout

def user_signup(request):
    if request.user.is_authenticated:
        return redirect('all_dishes')
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
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
def user_info(request):
    return render(request, 'users/info.html')

@login_required(login_url='user_login')
def user_history(request):
    return render(request, 'users/history.html')