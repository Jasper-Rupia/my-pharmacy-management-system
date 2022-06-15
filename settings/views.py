from django.http import HttpResponse
from django.template import loader


def pharmacy(request):
    authTemp = loader.get_template('advanced/page_pharmacy.html')
    return HttpResponse(authTemp.render())

def profile(request):
    authTemp = loader.get_template('advanced/page_profile.html')
    return HttpResponse(authTemp.render())

def users(request):
    authTemp = loader.get_template('advanced/page_users.html')
    return HttpResponse(authTemp.render())
