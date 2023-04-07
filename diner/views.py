from django.shortcuts import render, redirect
from diner.models import *
from django.contrib.auth.decorators import login_required

def main(request):
    return render(request, 'diner/main.html')