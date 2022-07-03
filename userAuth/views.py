
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from userAuth.models import ExtendUser


# def login(request):
#     # if request.session.has_key('user_email'):
#     #     email = request.session['user_email']
#     #     return redirect('dashboard:index')
#     if request.method == 'POST':
#         email = request.POST['email']  
#         password = request.POST['password']
#         try:
    #         user = User.objects.get(email=email)
    #         print(user.name) 
    #         print(user.password) 
    #         print(check_password(password, user.password))
    #         print(password)
    #         if user is not None:
    #             #request.session['user_email'] = user.email
    #             return redirect('dashboard:index')
    #     except:
    #         messages.success(request, ('Email or Password incorrect')) 
    #         return redirect('signin')
#     else:
#         return render(request, 'userAuth/page_login.html')


# def logout(request):
#     # try:
#     #     del request.session['user_email']
#     # except:
#     #     pass
#     return redirect('signin')


def user_login(request):
    if request.user.is_authenticated:
        return redirect('dashboard:index')
    elif request.method == "POST":
        username = request.POST['username']   
        password = request.POST['password']  
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard:index')
        else:
            messages.success(request, ('Username or Password incorrect')) 
            return redirect('signin')
    else:
        return render(request, 'userAuth/page_login.html')


def user_logout(request):
    if request.method == "POST":
        logout(request)
        return redirect('signin')


def newPassword(request):
    return render(request, 'userAuth/page_new_password.html')


def recover(request):
    return render(request, 'userAuth/page_recover.html')


def register(request):
    return render(request, 'userAuth/page_reg.html')


def registerUser(request):
    if request.method == 'POST':
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        password = make_password(password)
        query = User(
                    username = username,
                    password = password,
                    email = email,
                    is_superuser = True,
                    is_staff = True
                )
        try:
            query.save()
        except:
            messages.success(request, ('Username already taken!. Change it.')) 
            return redirect('register')
        
        user = User.objects.get(username=username)
        query = ExtendUser(
                id = user, 
                work_for = user,
                title = 'owner',
            ) 
        query.save()

    return redirect('signin')