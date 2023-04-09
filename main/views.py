from django.shortcuts import render, redirect
from main.models import *
from django.contrib.auth.decorators import login_required

def main(request):
    return render(request, 'main/main.html')

def all_dishes(request):
    dishes_list = Dish.objects.all()
    categories_list = Category.objects.all()
    return render(request, 'main/dishes.html', {'dishes_list':dishes_list, 'categories_list':categories_list})

def category_dishes(request, category_id):
    chosen_category = Category.objects.get(id=category_id)
    dishes_list = chosen_category.dish_set.all()
    categories_list = Category.objects.all()
    return render(request, 'main/dishes.html', {'dishes_list':dishes_list, 'categories_list':categories_list})

@login_required(login_url='user_login')
def fill_order(request):
    return render(request, 'main/order.html')

@login_required(login_url='user_login')
def show_delivery(request):
    return render(request, 'main/delivery.html')