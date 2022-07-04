from turtle import title
from django.shortcuts import render, redirect
from .models import Pharmacy
from django.contrib.auth.decorators import login_required
from userAuth.models import pmsUser
from django.contrib.auth.hashers import make_password
from django.contrib import messages


def pharmacy(request):
    pharmacy_values = Pharmacy.objects.filter(owner = request.user.work_for)
    varToPass = {
        'pharmacy_values': pharmacy_values,
    }
    return render(request, 'advanced/page_pharmacy.html', varToPass)
    

@login_required(login_url='')
def addPharmacy(request):
    query = Pharmacy(   name = request.GET['name'],
                        location = request.GET['address'],
                        owner = request.user,
                    )
    query.save()
    return redirect('settings:pharmacy')


@login_required(login_url='')
def delPharmacy(request, id):  
    query = Pharmacy.objects.get(id = id)  
    query.delete()  
    return redirect('settings:pharmacy')


def updPharmacy(request):
    id = request.GET['id']
    query = Pharmacy.objects.get(id=id)
    query.name = request.GET['name']
    query.location = request.GET['address']
    query.save()
    return redirect('settings:pharmacy')


@login_required(login_url='')
def profile(request):
    extend_user_value = pmsUser.objects.get(id=request.user.id)
    varToPass = { 
        'extend_user_value': extend_user_value
    }
    return render(request, 'advanced/page_profile.html', varToPass)
    

@login_required(login_url='')
def users(request):
    user_values = pmsUser.objects.filter(work_for=request.user.work_for)
    varToPass = { 
        'user_values': user_values,
    }
    return render(request, 'advanced/page_users.html', varToPass)


@login_required(login_url='')
def addUsers(request):
    if request.method == 'POST':
        email = request.POST['email']
        username = request.POST['username']
        password = make_password(username)
        title = request.POST['title']
        if title == 'partner':
            is_superuser = True
        else:
            is_superuser = False
        query = pmsUser(
                    username = username,
                    password = password,
                    email = email,
                    title = title,
                    work_for = request.user.work_for,
                    is_superuser = is_superuser,
                    is_staff = True
                )
        query.save()

    return redirect('settings:users') 
    

@login_required(login_url='')
def delUsers(request):  
    ids  = request.GET.getlist('id')
    for id in ids:
        query = pmsUser.objects.get(id = id)
        query.delete()  
    return redirect('settings:users')