from xml.dom.minidom import Element
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Records
from settings.models import Pharmacy

    
@login_required(login_url='')
def receipt(request):
    if request.method == 'POST':
        sell_item_ids = request.POST.getlist('sell_item_id')
        sell_item_count = len(sell_item_ids)
        total = request.POST.getlist('total')[0]
        total = float(total.replace(',', ''))
        customer_name = request.POST['customer_name']
        customer_tel = request.POST['customer_tel']
        pharmacy_value = Pharmacy.objects.get(owner = request.user.work_for)
        query = Records(customer = customer_name,
                        contact = customer_tel,
                        items = sell_item_count,
                        total_amount = total,
                        trans_by = request.user,
                        in_pharmacy = pharmacy_value,
                        owner = request.user.work_for
                        )
        query.save()
        return render(request, 'advanced/page_receipt.html')
    return redirect('sales:records')


@login_required(login_url='')
def records(request):
    sales_records = Records.objects.filter(owner=request.user.work_for)
    return render(request, 'advanced/page_sales_records.html', {'sales_records': sales_records})

@login_required(login_url='')
def sell(request):
    return render(request, 'advanced/page_sell.html')
    

