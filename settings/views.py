from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse


def pharmacy(request):
    return render(request, 'advanced/page_pharmacy.html')
    

def profile(request):
    return render(request, 'advanced/page_profile.html')
    

def users(request):
    return render(request, 'advanced/page_users.html')
    
