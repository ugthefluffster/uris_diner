from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from main.models import *
from .forms import *

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
            return redirect('show_delivery')
    return render(request, 'main/order.html', {'form':form})

@login_required(login_url='user_login')
def show_delivery(request):
    open_deliveries = Delivery.objects.filter(order__user=request.user).filter(is_delivered=False)    
    return render(request, 'main/delivery.html', {'open_deliveries':open_deliveries})