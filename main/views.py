from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from main.models import *
from main.forms import *

def main(request):
    return render(request, 'main/landing.html')

def menu_all_categories(request):
    categories_list = sorted(Category.objects.filter(is_deleted=False), key=lambda category: category.position)
    return render(request, 'main/menu_all_categories.html', {
        'categories_list':categories_list})

def menu_category_dishes(request, category_id):
    categories_list = sorted(Category.objects.filter(is_deleted=False), key=lambda category: category.position)
    try:
      category = Category.objects.get(id=category_id)
    except:
        return redirect('menu_all_categories')
    show_dishes = Dish.objects.filter(category=category, is_deleted=False)
    form = ItemAmountForm()
    return render(request, 'main/menu_category_dishes.html', {
        'categories_list':categories_list, 
        'show_dishes':show_dishes, 
        'category': category,
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
    open_orders = sorted(request.user.cart_set.filter(delivery__is_delivered=False), key=lambda order: order.delivery.created, reverse=True)   
    return render(request, 'main/delivery.html', {'open_orders':open_orders})

@login_required(login_url='user_login')
def add_to_cart(request):
    if request.method == 'POST':
        form = ItemAmountForm(request.POST)
        if form.is_valid():
            try:
                dish = Dish.objects.get(id=request.POST['dish_id'])
            except:
                return redirect('menu_all_categories')
            if request.user.is_staff:
                messages.info(request, f'Staff cannot place orders.')
            else:
                amount = request.POST['amount']
                cart = request.user.cart_set.last()
                new_item = Item(
                    dish = dish, 
                    cart = cart,
                    amount = amount)
                new_item.save()
                messages.info(request, f'{amount} X {dish.name} added to cart')
    return redirect('menu_category_dishes', category_id=dish.category.id)

@login_required(login_url='user_login')
def show_cart(request):
    cart = request.user.cart_set.last()
    return render(request, 'main/cart.html', {'cart':cart})

@login_required(login_url='user_login')
def change_cart_item(request):
    if request.method == 'POST':
        try:
            item = Item.objects.get(id=request.POST['item_id'])
        except:
            return redirect('show_cart')
        print(request.POST)
        item.amount += int(request.POST['amount'])
        if item.amount > 0:
            item.save()
    return redirect('show_cart')

@login_required(login_url='user_login')
def delete_cart_item(request):
    if request.method == 'POST':
        try:
            item = Item.objects.get(id=request.POST['item_id'])
        except:
            return redirect('show_cart')
        item.delete()
    return redirect('show_cart')