from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from userAuth.models import ExtendUser


@login_required(login_url='')
def receipt(request):
    return render(request, 'advanced/page_receipt.html')
    

@login_required(login_url='')
def records(request):
    extend_user_value = ExtendUser.objects.get(id=request.user.id)
    varToPass = { 
        'extend_user_value': extend_user_value
    }
    return render(request, 'advanced/page_sales_records.html', varToPass)
    

@login_required(login_url='')
def sell(request):
    extend_user_value = ExtendUser.objects.get(id=request.user.id)
    varToPass = { 
        'extend_user_value': extend_user_value
    }
    return render(request, 'advanced/page_sell.html', varToPass)
    

