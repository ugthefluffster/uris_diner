from django.shortcuts import render, redirect
from django.contrib.admin.views.decorators import staff_member_required
from main.models import *
from .forms import CategoryForm

@staff_member_required(login_url='backoffice_login')
def show_categories(request):
    all_categories = Category.objects.all()
    return render(request, 'categories/show_categories.html', {'all_categories':all_categories})

@staff_member_required(login_url='backoffice_login')
def add_category(request):
    form = CategoryForm()
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show_categories')
    return render(request, 'categories/add_category.html', {'form':form})

@staff_member_required(login_url='backoffice_login')
def edit_category(request, id):
    category = Category.objects.get(id=id)
    form = CategoryForm(instance=category)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('show_categories')
    return render(request, 'categories/edit_category.html', {'form':form, 'category':category})

@staff_member_required(login_url='backoffice_login')
def delete_category(request, id):
    category = Category.objects.get(id=id)
    if request.method == 'POST':
        category.delete()
        return redirect('show_categories')
    return render(request, 'categories/delete_category.html', {'category':category})

