
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse


def user_login(request):
    if request.method == "POST":
        username = request.POST['username']  
        password = request.POST['password']  
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            # if request.GET.get('next', None):
            #     return HttpResponseRedirect(request.GET['next'])
            # else:
            #     return redirect('dashboard:index')
            return redirect('dashboard:index')
        else:
            messages.success(request, ('Username or Password incorrect')) 
            return redirect('log')
    else:
        return render(request, 'userAuth/page_login.html')


def user_logout(request):
    if request.method == "POST":
        logout(request)
        return redirect('log')


def newPassword(request):
    return render(request, 'userAuth/page_new_password.html')


def recover(request):
    return render(request, 'userAuth/page_recover.html')


def register(request):
    return render(request, 'userAuth/page_register.html')
