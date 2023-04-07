from django.shortcuts import render, redirect
from diner.models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test

# test_func
def check_if_staff(user):
    return user.is_staff == True

def backoffice_login(request):
    return render(request, 'backoffice/staff_login.html')

@login_required(login_url='backoffice_login')
@user_passes_test(check_if_staff, login_url='backoffice_login')
def manage_deliveries(request):
    return render(request, 'backoffice/manage_deliveries.html')

@login_required(login_url='backoffice_login')
@user_passes_test(check_if_staff, login_url='backoffice_login')
def manage_categories(request):
    return render(request, 'backoffice/manage_categories.html')

@login_required(login_url='backoffice_login')
@user_passes_test(check_if_staff, login_url='backoffice_login')
def manage_dishes(request):
    return render(request, 'backoffice/manage_dishes.html')