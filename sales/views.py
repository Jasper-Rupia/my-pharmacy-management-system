from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse


def receipt(request):
    return render(request, 'advanced/page_receipt.html')
    

def records(request):
    return render(request, 'advanced/page_sales_records.html')
    

def sell(request):
    return render(request, 'advanced/page_sell.html')
    

