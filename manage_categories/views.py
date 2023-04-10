from django.shortcuts import render, redirect
from django.contrib.admin.views.decorators import staff_member_required
from main.models import *


@staff_member_required(login_url='backoffice_login')
def show_categories(request):
    all_categories = Category.objects.all()
    return render(request, 'categories/show_categories.html', {'all_categories':all_categories})

@staff_member_required(login_url='backoffice_login')
def add_category(request):
    pass

@staff_member_required(login_url='backoffice_login')
def edit_category(request):
    pass

@staff_member_required(login_url='backoffice_login')
def delete_category(request):
    pass

