from django.http import HttpResponse
from django.template import loader


def pharmacy(request):
    pmsTemplate = loader.get_template('advanced/page_pharmacy.html')
    return HttpResponse(pmsTemplate.render())

def profile(request):
    pmsTemplate = loader.get_template('advanced/page_profile.html')
    return HttpResponse(pmsTemplate.render())

def users(request):
    pmsTemplate = loader.get_template('advanced/page_users.html')
    return HttpResponse(pmsTemplate.render())
