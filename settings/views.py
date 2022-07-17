
from django.shortcuts import render, redirect
from .models import Pharmacy
from django.contrib.auth.decorators import login_required
from userAuth.models import pmsUser
from django.contrib.auth.hashers import make_password, check_password
from django.contrib import messages


@login_required(login_url='')
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

@login_required(login_url='')
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
def updateDp(request):
    query = pmsUser.objects.get(id=request.user.id)
    if 'update_dp' in request.POST: 
        query.avata = request.FILES['avata']
        query.save()
    elif 'reset_dp' in request.POST:
        query.avata = 'users_dp/no-profile.jpg'
        query.save()
    return redirect('settings:profile')


@login_required(login_url='')
def updProfile(request):
    query = pmsUser.objects.get(id=request.user.id)
    query.username = request.GET['username']
    query.email = request.GET['email']
    query.tel = request.GET['tel']
    query.save()
    return redirect('settings:profile')
    

@login_required(login_url='')
def updPassword(request):
    if request.method == 'POST': 
        oldPassword = request.POST['oldPassword'] 
        check = check_password(oldPassword, request.user.password) 
        if check: 
            newPassword = request.POST['newPassword'] 
            confirmPassword = request.POST['confirmPassword'] 
            if newPassword == confirmPassword: 
                password = make_password(newPassword) 
                query = pmsUser.objects.get(id=request.user.id) 
                query.password = password 
                query.save() 
                #messages.success(request, ('Password updated')) 
                return redirect('settings:profile') 
            else: 
                messages.warning(request, ('New Password & Confirm didn\'t match')) 
                return redirect('settings:profile') 
        else: 
            messages.warning(request, ('Old Password incorrect!')) 
            return redirect('settings:profile') 


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