from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from main.models import *
from main.forms import *

def main(request):
    return render(request, 'main/landing.html')

def all_dishes(request):
    categories_list = Category.objects.filter(is_deleted=False)
    form = ItemAmountForm()
    return render(request, 'main/all_dishes.html', {
        'categories_list':categories_list, 
        'form':form})

def category_dishes(request, category_id):
    categories_list = Category.objects.filter(is_deleted=False)
    category = Category.objects.get(id=category_id)
    show_dishes = Dish.objects.filter(category=category, is_deleted=False)
    form = ItemAmountForm()
    return render(request, 'main/category_dishes.html', {
        'categories_list':categories_list, 
        'show_dishes':show_dishes, 
        'form':form})

@login_required(login_url='user_login')
def fill_order(request):
    form = OrderForm()
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            cart = request.user.cart_set.last()
            new_delivery = Delivery(
                address = form.cleaned_data['address'],
                comment = form.cleaned_data['comment'],
                order = cart)
            new_delivery.save()
            new_cart = Cart(user = request.user)
            new_cart.save()
            messages.info(request, 
                f'Thank you {request.user.first_name.title()}! Your order number {new_delivery.order_id} have been recieved and is on its way.')
            return redirect('show_delivery')
    return render(request, 'main/order.html', {'form':form})

@login_required(login_url='user_login')
def show_delivery(request):
    open_orders = Delivery.objects.filter(order__user=request.user).filter(is_delivered=False)  
    open_orders = sorted(request.user.cart_set.filter(delivery__is_delivered=False), key=lambda order: order.delivery.created)   
    return render(request, 'main/delivery.html', {'open_orders':open_orders})