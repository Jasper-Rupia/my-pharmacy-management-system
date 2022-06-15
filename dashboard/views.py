from django.http import HttpResponse
from django.template import loader


def index(request):
    authTemp = loader.get_template('advanced/index.html')
    return HttpResponse(authTemp.render())