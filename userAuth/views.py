from django.shortcuts import render

# Create your views here.
# def index(request):
#     authTemp = loader.get_template('index.html')
#     return HttpResponse(authTemp.render())

def index(request):
    return render(request, 'index.html')

def newPassword(request):
    return render(request, 'page_new_password.html')

def recover(request):
    return render(request, 'page_recover.html')

def register(request):
    return render(request, 'page_register.html')
