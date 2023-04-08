from django.shortcuts import render, redirect
from diner.models import *
from django.contrib.admin.views.decorators import staff_member_required


def backoffice_login(request):
    return render(request, 'backoffice/staff_login.html')

@staff_member_required(login_url='backoffice_login')
def manage_deliveries(request):
    return render(request, 'backoffice/manage_deliveries.html')

@staff_member_required(login_url='backoffice_login')
def manage_categories(request):
    return render(request, 'backoffice/manage_categories.html')

@staff_member_required(login_url='backoffice_login')
def manage_dishes(request):
    return render(request, 'backoffice/manage_dishes.html')