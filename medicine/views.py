from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from medicine.models import Category, Stock
from settings.models import Pharmacy
from datetime import date
#from django.db import connection


@login_required(login_url='')
def category(request):
    try:
        pharmacy_value = Pharmacy.objects.get(owner = request.user.work_for)
    except:
        varToPass = {
            'pharmacy_value': 0
        }
        return render(request, 'advanced/page_category.html', varToPass)
    category_values = Category.objects.filter(in_pharmacy=pharmacy_value)
    stock_values = Stock.objects.filter(in_pharmacy=pharmacy_value)
    today = date.today().isoformat()
    varToPass = {
        'category_values': category_values,
        'stock_values': stock_values,
        'today': today
    }
    return render(request, 'advanced/page_category.html', varToPass)


@login_required(login_url='')
def addCategory(request):
    category_name = request.GET['category_name']
    pharmacy_value = Pharmacy.objects.get(owner = request.user.work_for)
    query = Category(   name = category_name,
                        in_pharmacy = pharmacy_value,
                        owner = request.user.work_for
                        )
    query.save()
    #print(connection.queries)
    #print(category_values)
    return redirect('medicine:category')


@login_required(login_url='')
def delCategory(request):  
    category_ids  = request.GET.getlist('category_id')
    for category_id in category_ids:
        query = Category.objects.get(id = category_id)  
        query.delete() 
    return redirect('medicine:category')


@login_required(login_url='')
def stock(request):
    try:
        pharmacy_value = Pharmacy.objects.get(owner = request.user.work_for)
    except:
        varToPass = {
            'pharmacy_value': 0
        }
        return render(request, 'advanced/page_stock.html', varToPass)
    category_values = Category.objects.filter(in_pharmacy=pharmacy_value)
    stock_values = Stock.objects.filter(in_pharmacy=pharmacy_value)
    varToPass = {
        'category_values': category_values,
        'stock_values': stock_values,
    }
    return render(request, 'advanced/page_stock.html', varToPass)


@login_required(login_url='')
def addStock(request):  
    pharmacy_value = Pharmacy.objects.get(owner = request.user.work_for)
    category_id = request.GET['category_id']
    category_id = Category.objects.get(id = category_id)
    query = Stock(  name = request.GET['medicine_name'], 
                    generic_name = request.GET['generic_name'],
                    quantity = request.GET['quantity'], 
                    packaging = request.GET['packaging'], 
                    cost = request.GET['cost'],
                    price = request.GET['price'], 
                    best_before = request.GET['best_before'],
                    category_name = category_id, 
                    in_pharmacy = pharmacy_value,
                    owner = request.user.work_for
                )
    query.save()
    return redirect('medicine:stock')


@login_required(login_url='')
def delStock(request):  
    medicine_names  = request.GET.getlist('medicine_name')
    for medicine_name in medicine_names:
        query = Stock.objects.get(name = medicine_name)  
        query.delete()  
    return redirect('medicine:stock')


