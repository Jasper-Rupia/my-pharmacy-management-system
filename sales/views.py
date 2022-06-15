from django.http import HttpResponse
from django.template import loader


def receipt(request):
    pmsTemplate = loader.get_template('advanced/page_receipt.html')
    return HttpResponse(pmsTemplate.render())

def records(request):
    pmsTemplate = loader.get_template('advanced/page_sales_records.html')
    return HttpResponse(pmsTemplate.render())

def sell(request):
    pmsTemplate = loader.get_template('advanced/page_sell.html')
    return HttpResponse(pmsTemplate.render())

