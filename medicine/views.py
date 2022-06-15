from django.http import HttpResponse
from django.template import loader

def category(request):
    pmsTemplate = loader.get_template('advanced/page_category.html')
    return HttpResponse(pmsTemplate.render())
    
def stock(request):
    pmsTemplate = loader.get_template('advanced/page_stock.html')
    return HttpResponse(pmsTemplate.render())
