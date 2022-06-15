from django.http import HttpResponse
from django.template import loader


def receipt(request):
    authTemp = loader.get_template('advanced/page_receipt.html')
    return HttpResponse(authTemp.render())

def sales_records(request):
    authTemp = loader.get_template('advanced/page_sales_records.html')
    return HttpResponse(authTemp.render())

def sell(request):
    authTemp = loader.get_template('advanced/page_sell.html')
    return HttpResponse(authTemp.render())

