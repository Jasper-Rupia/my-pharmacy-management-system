from django.shortcuts import render
from medicine.models import Category, Stock
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.db import connection


def category(request):
    category_values = Category.objects.all()
    stock_values = Stock.objects.all()
    varToPass = {
        'category_values': category_values,
        'stock_values': stock_values
    }
    return render(request, 'advanced/page_category.html', varToPass)


def addCategory(request):
    category_name = request.GET['category_name']
    query = Category(name = category_name)
    query.save()
    #print(connection.queries)
    #print(category_values)
    return HttpResponseRedirect(reverse('category'))


def delCategory(request):  
    category_name  = request.GET.getlist('category_name')
    for x in category_name:
        query = Category.objects.get(name = x)  
        query.delete()  
    return HttpResponseRedirect(reverse('category'))


def stock(request):
    medicine_name = 'panadol5'
    generic_name = 'paracetamo'
    packaging = '10'
    quantity = '15'
    cost = 1000
    price = 2200
    best_before = '2022-07-07'
    category_name = 'dawa1'
    query = Stock(  name = medicine_name, 
                    generic_name = generic_name, 
                    packaging = packaging, 
                    quantity = quantity,
                    cost = cost, 
                    price = price, 
                    best_before = best_before,
                    category_name_id = category_name
                    )
    query.save()
    return render(request, 'advanced/page_stock.html')
