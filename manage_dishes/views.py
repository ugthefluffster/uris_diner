from django.shortcuts import render, redirect
from django.contrib.admin.views.decorators import staff_member_required
from main.models import *

@staff_member_required(login_url='backoffice_login')
def show_dishes(request):
    all_dishes = Dish.objects.all()
    return render(request, 'dishes/show_dishes.html', {'all_dishes':all_dishes})

@staff_member_required(login_url='backoffice_login')
def add_dish(request):
    pass

@staff_member_required(login_url='backoffice_login')
def edit_dish(request):
    pass

@staff_member_required(login_url='backoffice_login')
def delete_dish(request):
    pass
