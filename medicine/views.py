from django.shortcuts import render
from medicine.models import Category, Stock
from django.template import loader
from django.http import HttpResponse
from django.db import connection


def category(request):
    #x = request.GET['fname']
    category_name = "dawa2"
    query = Category(name = category_name)
    query.save()
    category_values = Category.objects.all()
    varToPass = {
        'category_values': category_values
    }
    # print(connection.queries)
    # print(category_values)
    return render(request, 'advanced/page_category.html', varToPass)


def stock(request):
    medicine_name = 'panadol1'
    generic_name = 'paracetamo'
    packaging = '10'
    quantity = '15'
    cost = 1000
    price = 2200
    best_before = '2022-07-07'
    category_name = 'dawa2'
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
