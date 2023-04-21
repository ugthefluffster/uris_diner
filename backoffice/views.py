from django.shortcuts import render, redirect
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import login, logout
from main.models import *
from main.forms import *

def backoffice_login(request):
    if request.user.is_authenticated and request.user.is_staff==True:
        return redirect('manage_orders')
    form = CustomAuthenticationForm()
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if request.POST['next']:
                return redirect(request.POST['next'])
            return redirect('manage_orders')
    return render(request, 'backoffice/staff_login.html', {'form':form})

@staff_member_required(login_url='backoffice_login')
def backoffice_logout(request):
    logout(request)
    return redirect('main')

@staff_member_required(login_url='backoffice_login')
def manage_orders(request):
    orders_list = sorted(Cart.objects.filter(delivery__is_delivered=False), key=lambda order: order.delivery.created)
    if request.method == 'POST':
        fulfilled_order = Delivery.objects.get(order_id=request.POST['order_id'])
        fulfilled_order.is_delivered = True
        fulfilled_order.save()
        return redirect('manage_orders')
    return render(request, 'backoffice/manage_orders.html', {'orders_list':orders_list})

@staff_member_required(login_url='backoffice_login')
def show_orders_history(request):
    orders_list = sorted(Cart.objects.filter(delivery__is_delivered=True), key=lambda order: order.delivery.created, reverse=True)
    return render(request, 'backoffice/orders_history.html', {'orders_list':orders_list})

@staff_member_required(login_url='backoffice_login')
def add_category(request):
    form = CategoryForm()
    if request.method == 'POST':
        form = CategoryForm(request.POST, request.FILES)
        if form.is_valid():
            new_category = form.save()
            category_list = Category.objects.filter(is_deleted=False)
            new_category.position = len(category_list) - 1
            new_category.save()
            return redirect('menu_all_categories')
    return render(request, 'backoffice/add_category.html', {'form':form})

@staff_member_required(login_url='backoffice_login')
def edit_category(request, id):
    try:
        category = Category.objects.get(id=id)
    except:
        return redirect('menu_all_categories')
    form = CategoryForm(instance=category)
    if request.method == 'POST':
        form = CategoryForm(request.POST, request.FILES, instance=category)
        if form.is_valid():
            form.save()
            return redirect('menu_all_categories')
    return render(request, 'backoffice/edit_category.html', {'form':form, 'category':category})

@staff_member_required(login_url='backoffice_login')
def category_up(request, id):
    try:
        category = Category.objects.get(id=id)
    except:
        return redirect('menu_all_categories')
    category_list = sorted(Category.objects.filter(is_deleted=False), key=lambda category: category.position)
    prev = category_list[category.position-1]
    if request.method == 'POST':
        category.position, prev.position = prev.position, category.position
        category.save()
        prev.save()
    return redirect('menu_all_categories')

@staff_member_required(login_url='backoffice_login')
def category_down(request, id):
    try:
        category = Category.objects.get(id=id)
    except:
        return redirect('menu_all_categories')
    category_list = sorted(Category.objects.filter(is_deleted=False), key=lambda category: category.position)
    prev = category_list[category.position+1]
    if request.method == 'POST':
        category.position, prev.position = prev.position, category.position
        category.save()
        prev.save()
    return redirect('menu_all_categories')

@staff_member_required(login_url='backoffice_login')
def delete_category(request, id):
    try:
        category = Category.objects.get(id=id)
    except:
        return redirect('menu_all_categories')
    if request.method == 'POST':
        category.is_deleted = True
        category.position = -1
        category.save()
        for dish in category.dish_set.all():
            dish.is_deleted = True
            dish.save()
        category_list = sorted(Category.objects.filter(is_deleted=False), key=lambda category: category.position)
        new_position = 0
        for category_obj in category_list:
            category_obj.position = new_position
            category_obj.save()
            new_position += 1
        return redirect('menu_all_categories')
    return render(request, 'backoffice/delete_category.html', {'category':category})

@staff_member_required(login_url='backoffice_login')
def add_dish(request):
    form = DishForm()
    if request.method == 'POST':
        form = DishForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('menu_category_dishes', category_id=form.instance.category.id)
    return render(request, 'backoffice/add_dish.html', {'form':form})

@staff_member_required(login_url='backoffice_login')
def edit_dish(request, id):
    try:
        dish = Dish.objects.get(id=id)
    except:
        return redirect('menu_all_categories')
    form = DishForm(instance=dish)
    if request.method == 'POST':
        form = DishForm(request.POST, request.FILES, instance=dish)
        if form.is_valid():
            form.save()
            return redirect('menu_category_dishes', category_id=dish.category.id)
    return render(request, 'backoffice/edit_dish.html', {'form':form, 'dish':dish})

@staff_member_required(login_url='backoffice_login')
def delete_dish(request, id):
    try:
        dish = Dish.objects.get(id=id)
    except:
        return redirect('menu_all_categories')
    if request.method == 'POST':
        dish.is_deleted = True
        dish.save()
        return redirect('menu_category_dishes', category_id=dish.category.id)
    return render(request, 'backoffice/delete_dish.html', {'dish':dish})

