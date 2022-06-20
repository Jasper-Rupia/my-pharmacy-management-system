from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse


def login(request):
    return render(request, 'userAuth/index.html')


def newPassword(request):
    return render(request, 'userAuth/page_new_password.html')


def recover(request):
    return render(request, 'userAuth/page_recover.html')


def register(request):
    return render(request, 'userAuth/page_register.html')
