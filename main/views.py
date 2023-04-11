from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from main.models import *
from main.forms import *

def main(request):
    return render(request, 'main/main.html')

def all_dishes(request):
    categories_list = Category.objects.filter(is_deleted=False)
    show_categories = categories_list
    form = ItemAmountForm()
    rendered_form = form.render('main/form_templates/input_form.html')
    return render(request, 'main/dishes.html', {
        'categories_list':categories_list, 
        'show_categories':show_categories,
        'form':rendered_form})

def category_dishes(request, category_id):
    categories_list = Category.objects.filter(is_deleted=False)
    show_categories = [Category.objects.get(id=category_id)]
    return render(request, 'main/dishes.html', {'categories_list':categories_list, 'show_categories':show_categories})

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
    rendered_form = form.render('main/form_templates/input_form.html')
    return render(request, 'main/order.html', {'form':rendered_form})

@login_required(login_url='user_login')
def show_delivery(request):
    open_orders = Delivery.objects.filter(order__user=request.user).filter(is_delivered=False)  
    open_orders = sorted(request.user.cart_set.filter(delivery__is_delivered=False), key=lambda order: order.delivery.created)   
    return render(request, 'main/delivery.html', {'open_orders':open_orders})