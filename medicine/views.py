from django.shortcuts import render
from medicine.models import Category, Stock
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
#from django.db import connection

@login_required(login_url='/login')
def category(request):
    category_values = Category.objects.all().order_by('-date_created')
    stock_values = Stock.objects.all()
    varToPass = {
        'category_values': category_values,
        'stock_values': stock_values
    }
    return render(request, 'advanced/page_category.html', varToPass)


@login_required(login_url='/login')
def addCategory(request):
   # category_name = request.GET['category_name']
    query = Category(name = request.GET['category_name'])
    query.save()
    #print(connection.queries)
    #print(category_values)
    return HttpResponseRedirect(reverse('category'))


@login_required(login_url='/login')
def delCategory(request):  
    category_names  = request.GET.getlist('category_name')
    for category_name in category_names:
        query = Category.objects.get(name = category_name)  
        query.delete()  
    return HttpResponseRedirect(reverse('category'))


@login_required(login_url='/login')
def stock(request):
    category_values = Category.objects.all()
    stock_values = Stock.objects.all().order_by('-date_created')
    varToPass = {
        'category_values': category_values,
        'stock_values': stock_values
    }
    return render(request, 'advanced/page_stock.html', varToPass)


@login_required(login_url='/login')
def addStock(request):  
    medicine_name = request.GET['medicine_name']  
    generic_name = request.GET['generic_name']
    query = Stock(  name = medicine_name, 
                    generic_name = generic_name,
                    quantity = request.GET['quantity'], 
                    packaging = request.GET['packaging'], 
                    cost = request.GET['cost'], 
                    price = request.GET['price'], 
                    best_before = request.GET['best_before'],
                    category_name_id = request.GET['category_name']
                )
    query.save()
    return HttpResponseRedirect(reverse('stock'))


@login_required(login_url='/login')
def delStock(request):  
    medicine_names  = request.GET.getlist('medicine_name')
    for medicine_name in medicine_names:
        query = Stock.objects.get(name = medicine_name)  
        query.delete()  
    return HttpResponseRedirect(reverse('stock'))