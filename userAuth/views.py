from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
# def index(request):
#     authTemp = loader.get_template('index.html')
#     return HttpResponse(authTemp.render())

def index(request):
    return render(request, 'index.html')

def recover(request):
    return render(request, 'page_recover.html')

def register(request):
    return render(request, 'page_register.html')

def newPassword(request):
    return render(request, 'page_new-password.html')