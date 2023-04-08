from django.shortcuts import render, redirect
from diner.models import *
from django.contrib.auth.decorators import login_required

def main(request):
    return render(request, 'diner/main.html')

def all_dishes(request):
    dishes_list = Dish.objects.all()
    categories_list = Category.objects.all()
    return render(request, 'diner/dishes.html', {'dishes_list':dishes_list, 'categories_list':categories_list})

def category_dishes(request, category_id):
    chosen_category = Category.objects.get(id=category_id)
    dishes_list = chosen_category.dish_set.all()
    categories_list = Category.objects.all()
    return render(request, 'diner/dishes.html', {'dishes_list':dishes_list, 'categories_list':categories_list})

@login_required(login_url='user_login')
def add_to_cart(request):
    if request.method == 'POST':
        dish = Dish.objects.get(id=request.POST['dish_id'])
        cart = request.user.cart_set.last()
        new_item = Item(
            dish = dish, 
            cart=cart,
            amount=request.POST['amount'])
        new_item.save()
    return redirect('all_dishes')

@login_required(login_url='user_login')
def show_cart(request):
    cart = request.user.cart_set.last()
    return render(request, 'diner/cart.html', {'cart':cart})

@login_required(login_url='user_login')
def change_cart_item(request):
    if request.method == 'POST':
        item = Item.objects.get(id=request.POST['item_id'])
        item.amount = request.POST['amount']
        item.save()
    return redirect('show_cart')

@login_required(login_url='user_login')
def delete_cart_item(request):
    if request.method == 'POST':
        item = Item.objects.get(id=request.POST['item_id'])
        item.delete()
    return redirect('show_cart')

@login_required(login_url='user_login')
def fill_order(request):
    return render(request, 'diner/order.html')

@login_required(login_url='user_login')
def show_delivery(request):
    return render(request, 'diner/delivery.html')