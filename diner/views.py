from django.shortcuts import render, redirect
from diner.models import *
from django.contrib.auth.decorators import login_required

def main(request):
    return render(request, 'diner/main.html')

def all_dishes(request):
    return render(request, 'diner/dishes.html')

def category_dishes(request, category_id):
    return render(request, 'diner/dishes.html')

@login_required(login_url='user_login')
def show_cart(request, cart_id):
    return render(request, 'diner/cart.html')

@login_required(login_url='user_login')
def fill_order(request, cart_id):
    return render(request, 'diner/order.html')

@login_required(login_url='user_login')
def show_delivery(request, order_id):
    return render(request, 'diner/delivery.html')