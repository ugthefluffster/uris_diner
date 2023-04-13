from django.shortcuts import render, redirect
from django.contrib.admin.views.decorators import staff_member_required
from main.models import *
from main.forms import *

@staff_member_required(login_url='backoffice_login')
def show_dishes(request):
    all_categories = Category.objects.filter(is_deleted=False)
    return render(request, 'manage_dishes/show_dishes.html', {'all_categories':all_categories})

@staff_member_required(login_url='backoffice_login')
def add_dish(request):
    form = DishForm()
    if request.method == 'POST':
        form = DishForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('show_dishes')

    return render(request, 'manage_dishes/add_dish.html', {'form':form})

@staff_member_required(login_url='backoffice_login')
def edit_dish(request, id):
    dish = Dish.objects.get(id=id)
    form = DishForm(instance=dish)
    if request.method == 'POST':
        form = DishForm(request.POST, request.FILES, instance=dish)
        if form.is_valid():
            form.save()
            return redirect('show_dishes')
    return render(request, 'manage_dishes/edit_dish.html', {'form':form, 'dish':dish})

@staff_member_required(login_url='backoffice_login')
def delete_dish(request, id):
    dish = Dish.objects.get(id=id)
    if request.method == 'POST':
        dish.is_deleted = True
        dish.save()
        return redirect('show_dishes')
    return render(request, 'manage_dishes/delete_dish.html', {'dish':dish})
