from email.mime import image
from typing import Counter
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from medicine.models import Category, Stock
from settings.models import Pharmacy
from django.db.models import Count
#from django.db import connection
from django.core.files.storage import FileSystemStorage
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.contrib import messages


@login_required(login_url='')
def category(request):
    try:
        pharmacy_value = Pharmacy.objects.get(owner = request.user.work_for)
    except:
        varToPass = {
            'pharmacy_value': 0
        }
        return render(request, 'advanced/page_category.html', varToPass)
    categories_in_pharmacy = Category.objects.filter(in_pharmacy=pharmacy_value).order_by('-date_modified')
    medicines_in_each_category = categories_in_pharmacy.annotate(medicines_in_category=Count('stock'))
    varToPass = {
        'medicines_in_each_category': medicines_in_each_category,
    }
    return render(request, 'advanced/page_category.html', varToPass)


@login_required(login_url='')
def addCategory(request):
    if request.method == 'POST': 
        category_name = request.POST['category_name']
        pharmacy_value = Pharmacy.objects.get(owner = request.user.work_for)
        try:
            category_image = request.FILES['category_image']
        except:
            query = Category(   name = category_name,
                            image = 'categories/default_category.jpg',
                            in_pharmacy = pharmacy_value,
                            owner = request.user.work_for
                            ) 
            query.save()
            return redirect('medicine:category')
        # fss = FileSystemStorage()
        # file = fss.save(category_image.name, category_image)
        query = Category(   name = category_name,
                            image = category_image,
                            in_pharmacy = pharmacy_value,
                            owner = request.user.work_for
                            ) 
        query.save()
    #print(connection.queries)
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
    #return render(request, 'advanced/page_stockCopy.html', varToPass)


@login_required(login_url='')
def addStock(request):  
    pharmacy_value = Pharmacy.objects.get(owner = request.user.work_for)
    name = request.GET['medicine_name']
    category_id = request.GET['category_id']
    category_id = Category.objects.get(id = category_id)
    query = Stock(  name = name, 
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


@login_required(login_url='')
def toUpdStock(request, id):
    try:
        pharmacy_value = Pharmacy.objects.get(owner = request.user.work_for)
    except:
        varToPass = {
            'pharmacy_value': 0
        }
        return render(request, 'advanced/page_stock.html', varToPass)
    category_values = Category.objects.filter(in_pharmacy=pharmacy_value)
    stock_value = Stock.objects.get(id=id)  
    varToPass = {
        'category_values': category_values,
        'stock_value': stock_value
    }
    return render(request, 'advanced/page_edit_stock.html', varToPass)


@login_required(login_url='')
def updStock(request):
    print(request.POST['id'])
    category = Category.objects.get(id=request.POST['category_id'])
    query = Stock.objects.get(id=request.POST['id'])  
    query.name = request.POST['medicine_name']
    query.generic_name = request.POST['generic_name']
    query.quantity = request.POST['quantity']
    query.packaging = request.POST['packaging'] 
    query.cost = request.POST['cost']
    query.price = request.POST['price'] 
    query.best_before = request.POST['best_before']
    query.category_name = category
    query.save() 
    return redirect('medicine:stock')


# # ajax crud table
# def fetchDataStock(request):
#     stock_values = Stock.objects.all()
#     value = ""
#     for instance in stock_values:
#         value += f'''
#             <tr>
#                 <td>{instance.id}</td>
#                 <td>{instance.name}</td>
#                 <td>{instance.generic_name}</td>
#                 <td>{instance.category_name.name}</td>
#                 <td>{instance.quantity} {instance.packaging}</td>
#                 <td>{instance.cost}</td>
#                 <td>{instance.price}</td>
#                 '''
#         if instance.is_exipired_medicine():
#             ex = f'''<td style="color: red;"> {instance.best_before} </td>'''
#         else:
#             ex = f'''<td> {instance.best_before} </td>'''
#         if instance.is_medicine_available():
#             av = f'''<td> <span class="badge rounded-pill bg-success"> Available </span> </td>''' 
#         else: 
#             av = f'''<td> <span class="badge rounded-pill bg-warning"> N/A </span> </td>'''
#         value = value + ex + av + f'''</tr>'''
#     return HttpResponse(value)


# @csrf_exempt
# def updStock(request):
#     id = request.POST.getlist('id')[0]
#     query = Stock.objects.get(id=id)  
#     # try:
#     #     name = request.POST.getlist('name')[0]
#     #     query.name = name 
#     #     query.save() 
#     # except:
#     #     pass
#     # try:
#     #     quantity = request.POST.getlist('quantity')[0]
#     #     query.quantity = quantity
#     #     query.save() 
#     # except:
#     #     pass
#     name = request.POST.getlist('name')[0]
#     query.name = name 
#     query.save() 
#     print('done new') 
#     return HttpResponse(request)