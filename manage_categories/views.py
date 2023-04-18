from django.shortcuts import render, redirect
from django.contrib.admin.views.decorators import staff_member_required
from main.models import *
from main.forms import *

@staff_member_required(login_url='backoffice_login')
def show_categories(request):
    all_categories = Category.objects.filter(is_deleted=False)
    return render(request, 'manage_categories/show_categories.html', {'all_categories':all_categories})

@staff_member_required(login_url='backoffice_login')
def add_category(request):
    form = CategoryForm()
    if request.method == 'POST':
        form = CategoryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('show_categories')
    return render(request, 'manage_categories/add_category.html', {'form':form})

@staff_member_required(login_url='backoffice_login')
def edit_category(request, id):
    try:
        category = Category.objects.get(id=id)
    except:
        return redirect('show_categories')
    form = CategoryForm(instance=category)
    if request.method == 'POST':
        form = CategoryForm(request.POST, request.FILES, instance=category)
        if form.is_valid():
            form.save()
            return redirect('show_categories')
    return render(request, 'manage_categories/edit_category.html', {'form':form, 'category':category})

@staff_member_required(login_url='backoffice_login')
def delete_category(request, id):
    try:
        category = Category.objects.get(id=id)
    except:
        return redirect('show_categories')
    if request.method == 'POST':
        category.is_deleted = True
        category.save()
        for dish in category.dish_set.all():
            dish.is_deleted = True
            dish.save()
        return redirect('show_categories')
    return render(request, 'manage_categories/delete_category.html', {'category':category})

