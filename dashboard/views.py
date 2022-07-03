from django.shortcuts import render
from medicine.models import Stock, Category
from userAuth.models import ExtendUser
from datetime import date
from django.contrib.auth.decorators import login_required


@login_required(login_url='')
def index(request):
    extend_user_value = ExtendUser.objects.get(id=request.user.id)
    category_values = Category.objects.all()
    stock_values = Stock.objects.all()
    user_values = ExtendUser.objects.filter(work_for=extend_user_value.work_for.id) 
    today = date.today().isoformat()
    exipire_values = Stock.objects.exclude(best_before__gt=today)
    out_of_stock_values = Stock.objects.filter(quantity=0)
    varToPass = {
        'extend_user_value': extend_user_value,
        'category_values': category_values,
        'stock_values': stock_values,
        'user_values': user_values,
        'exipire_values': exipire_values,
        'out_of_stock_values': out_of_stock_values
    }
    return render(request, 'advanced/index.html', varToPass)
    