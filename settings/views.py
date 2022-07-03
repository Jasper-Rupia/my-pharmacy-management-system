from turtle import title
from django.shortcuts import render, redirect
from .models import Pharmacy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from userAuth.models import ExtendUser
from django.contrib.auth.hashers import make_password
from django.contrib import messages


def pharmacy(request):
    print(request.user.username)
    print(request.user.id)
    pharmacy_values = Pharmacy.objects.all().order_by('-registerd_date')
    varToPass = {
        'pharmacy_values': pharmacy_values
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


@login_required(login_url='')
def profile(request):
    extend_user_value = ExtendUser.objects.get(id=request.user.id)
    varToPass = { 
        'extend_user_value': extend_user_value
    }
    return render(request, 'advanced/page_profile.html', varToPass)
    

@login_required(login_url='')
def users(request):
    extend_user_value = ExtendUser.objects.get(id=request.user.id)
    user_values = ExtendUser.objects.filter(work_for=extend_user_value.work_for.id).order_by('-id')
    varToPass = { 
        'user_values': user_values,
        'extend_user_value': extend_user_value
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
        query = User(
                    username = username,
                    password = password,
                    email = email,
                    is_superuser = is_superuser,
                    is_staff = True
                )
        try:
            query.save()
        except:
            messages.success(request, ('Username already taken!. Change it.')) 
            return redirect('settings:users')
        
        user = User.objects.get(username=username)
        query = ExtendUser(
                id = user,
                work_for = request.user,
                title = title,
            )
        query.save()
    return redirect('settings:users') 
    

@login_required(login_url='')
def delUsers(request):  
    ids  = request.GET.getlist('id')
    for id in ids:
        query = User.objects.get(id = id)  
        query.delete()  
    return redirect('settings:users')