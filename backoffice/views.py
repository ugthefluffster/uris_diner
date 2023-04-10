from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import login, authenticate, logout
from main.models import *

def backoffice_login(request):
    if request.user.is_authenticated and request.user.is_staff==True:
        return redirect('manage_orders')
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
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
    all_orders = Cart.objects.all()
    if request.method == 'POST':
        fulfilled_order = Delivery.objects.get(order_id=request.POST['order_id'])
        fulfilled_order.is_delivered = True
        fulfilled_order.save()
    return render(request, 'backoffice/manage_orders.html', {'all_orders':all_orders})
