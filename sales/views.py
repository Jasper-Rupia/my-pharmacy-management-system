from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required(login_url='/login')
def receipt(request):
    return render(request, 'advanced/page_receipt.html')
    

@login_required(login_url='/login')
def records(request):
    return render(request, 'advanced/page_sales_records.html')
    

@login_required(login_url='/login')
def sell(request):
    return render(request, 'advanced/page_sell.html')
    

