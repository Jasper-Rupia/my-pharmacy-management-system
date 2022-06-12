from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

# Create your views here.

def index(request):
    mysite = loader.get_template('index.html')
    return HttpResponse(mysite.render())
    #return render(request, '')