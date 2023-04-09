from django.shortcuts import render, redirect
from main.models import *
from django.contrib.auth.decorators import login_required

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
    return render(request, 'cart/cart.html', {'cart':cart})

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
