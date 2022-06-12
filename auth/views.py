from ast import Return
from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def index(request):
    authTemp = loader.get_template('index.html')
    return HttpResponse(authTemp.render())