from django.shortcuts import render
from medicine.models import Stock, Category
from settings.models import User
from django.utils.timezone import datetime
from datetime import date


def index(request):
    category_count = Category.objects.all().count()
    stock_count = Stock.objects.all().count()
    user_count = User.objects.all().count()
    today = date.today().isoformat()
    exipire_count = Stock.objects.exclude(best_before__gt=today).count()
    out_of_stock_count = Stock.objects.filter(quantity=0).count()
    varToPass = {
        'category_count': category_count,
        'stock_count': stock_count,
        'user_count': user_count,
        'exipire_count': exipire_count,
        'out_of_stock_count': out_of_stock_count
    }
    return render(request, 'advanced/index.html', varToPass)
    