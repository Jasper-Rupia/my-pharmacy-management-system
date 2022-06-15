from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader


def category(request):
    authTemp = loader.get_template('advanced/page_category.html')
    return HttpResponse(authTemp.render())

def pharmacy(request):
    authTemp = loader.get_template('advanced/page_pharmacy.html')
    return HttpResponse(authTemp.render())

def profile(request):
    authTemp = loader.get_template('advanced/page_profile.html')
    return HttpResponse(authTemp.render())

def receipt(request):
    authTemp = loader.get_template('advanced/page_receipt.html')
    return HttpResponse(authTemp.render())

def sales_records(request):
    authTemp = loader.get_template('advanced/page_sales_records.html')
    return HttpResponse(authTemp.render())

def sell(request):
    authTemp = loader.get_template('advanced/page_sell.html')
    return HttpResponse(authTemp.render())

def stock(request):
    authTemp = loader.get_template('advanced/page_stock.html')
    return HttpResponse(authTemp.render())

def users(request):
    authTemp = loader.get_template('advanced/page_users.html')
    return HttpResponse(authTemp.render())