from django.http import HttpResponse
from django.template import loader

def category(request):
    authTemp = loader.get_template('advanced/page_category.html')
    return HttpResponse(authTemp.render())
    
def stock(request):
    authTemp = loader.get_template('advanced/page_stock.html')
    return HttpResponse(authTemp.render())
