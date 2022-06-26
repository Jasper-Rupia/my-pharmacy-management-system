from django.shortcuts import render
from .models import User, Pharmacy
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required


@login_required(login_url='/login')
def pharmacy(request):
    user_values = User.objects.all()
    pharmacy_values = Pharmacy.objects.all().order_by('-registerd_date')
    varToPass = {
        'user_values': user_values,
        'pharmacy_values': pharmacy_values
    }
    return render(request, 'advanced/page_pharmacy.html', varToPass)
    

@login_required(login_url='/login')
def addPharmacy(request):
    #user = User.objects.first()
    #id = user['id']
    query = Pharmacy(   name = request.GET['name'], 
                        location = request.GET['address'],
                        #owner = id,
                    )
    query.save()
    return HttpResponseRedirect(reverse('pharmacy'))


@login_required(login_url='/login')
def delPharmacy(request, id):  
    query = Pharmacy.objects.get(id = id)  
    query.delete()  
    return HttpResponseRedirect(reverse('pharmacy'))


@login_required(login_url='/login')
def profile(request):
    return render(request, 'advanced/page_profile.html')
    

@login_required(login_url='/login')
def users(request):
    user_values = User.objects.all().order_by('-registerd_date')
    varToPass = {
        'user_values': user_values,
    }
    return render(request, 'advanced/page_users.html', varToPass)


@login_required(login_url='/login')
def addUsers(request):
    query = User(   email = request.GET['email'], 
                    name = request.GET['name'],
                    title = request.GET['title'], 
                )
    query.save()
    return HttpResponseRedirect(reverse('users'))
    

@login_required(login_url='/login')
def delUsers(request):  
    ids  = request.GET.getlist('id')
    for id in ids:
        query = User.objects.get(id = id)  
        query.delete()  
    return HttpResponseRedirect(reverse('users'))