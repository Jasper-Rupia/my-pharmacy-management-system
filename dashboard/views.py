from django.http import HttpResponse
from django.template import loader


def index(request):
    pmsTemplate = loader.get_template('advanced/index.html')
    return HttpResponse(pmsTemplate.render())