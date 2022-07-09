
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from userAuth.models import pmsUser
from django.views.decorators.csrf import csrf_exempt

#     # if request.session.has_key('user_email'):
#     #     email = request.session['user_email']
#     #     return redirect('dashboard:index')

# def logout(request):
#     # try:
#     #     del request.session['user_email']
#     # except:
#     #     pass
#     return redirect('signin')

@csrf_exempt
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
        query = pmsUser(
                    username = username,
                    password = password,
                    email = email,
                    title = 'owner',
                    is_superuser = True,
                    is_staff = True
                )
        query.save()
        pmsuser = pmsUser.objects.get(username=username)
        pmsuser.work_for = pmsuser
        pmsuser.save()

    return redirect('signin')