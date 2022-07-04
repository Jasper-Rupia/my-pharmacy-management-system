from django.shortcuts import render
from medicine.models import Stock, Category
from userAuth.models import pmsUser
from datetime import date
from django.contrib.auth.decorators import login_required


@login_required(login_url='')
def index(request):
    user_count = pmsUser.objects.filter(work_for=request.user.work_for).count()
    category_values = Category.objects.filter(owner=request.user.work_for)
    stock_values = Stock.objects.filter(owner=request.user.work_for)
    today = date.today().isoformat()
    exipire_values = stock_values.exclude(best_before__gt=today)
    out_of_stock_values = Stock.objects.filter(quantity=0, owner=request.user.work_for) 
    varToPass = {
        'category_values': category_values,
        'stock_values': stock_values,
        'exipire_values': exipire_values,
        'out_of_stock_values': out_of_stock_values,
        'user_count': user_count
    }
    return render(request, 'advanced/index.html', varToPass)
    