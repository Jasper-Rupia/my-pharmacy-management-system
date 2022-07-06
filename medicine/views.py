from typing import Counter
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from medicine.models import Category, Stock
from settings.models import Pharmacy
from django.db.models import Count
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
    categories_in_pharmacy = Category.objects.filter(in_pharmacy=pharmacy_value)
    medicines_in_each_category = categories_in_pharmacy.annotate(medicines_in_category=Count('stock'))
    
    varToPass = {
        'medicines_in_each_category': medicines_in_each_category,
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
def delSellStock(request):  
    if 'del' in request.POST:
        medicine_ids  = request.POST.getlist('medicine_id')
        for medicine_id in medicine_ids:
            query = Stock.objects.get(id = medicine_id) 
            query.delete() 
        return redirect('medicine:stock')
    if 'sell' in request.POST:
        medicine_ids  = request.POST.getlist('medicine_id')
        medicines_to_sell = Stock.objects.filter(id__in = medicine_ids)
        return render(request, 'advanced/page_sell.html', {'medicines_to_sell': medicines_to_sell})
    return redirect('medicine:stock')
