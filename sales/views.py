
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Records
from settings.models import Pharmacy
from medicine.models import Stock
from datetime import datetime
    

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
        now = datetime.now().strftime("%Y%m%d-%H%M%S-%f")

        query = Records(customer = customer_name,
                        invoice = now,
                        contact = customer_tel,
                        items = sell_item_count,
                        total_amount = total,
                        trans_by = request.user,
                        in_pharmacy = pharmacy_value,
                        owner = request.user.work_for
                    )
        query.save()

        sold_stock_values = Stock.objects.filter(id__in=sell_item_ids)
        sell_item_qtys = request.POST.getlist('qty')
        sell_item_prices = request.POST.getlist('price')
        
        objects = []
        # for i, medicine in zip(range(len(sold_stock_values)), sold_stock_values):
        #     objects.append({
        #         'rec_i': i+1,
        #         'rec_med': medicine.name,
        #         'rec_qty': sell_item_qtys[i],
        #         'rec_price': sell_item_prices[i],
        #         'rec_subTotal': int(sell_item_qtys[i]) * int(sell_item_prices[i])
        #     })
        #     medicine.quantity = medicine.quantity - int(sell_item_qtys[i])
        #     medicine.sold = int(sell_item_qtys[i])
        #     item.save()

        i = 1
        for medicine, qty, price in zip(sold_stock_values, sell_item_qtys, sell_item_prices):
            objects.append({
                'rec_i': i,
                'rec_med': medicine.name,
                'rec_qty': qty,
                'rec_price': price,
                'rec_subTotal': int(qty) * int(price)
            })
            i += 1
            medicine.quantity = medicine.quantity - int(qty)
            medicine.sold = medicine.sold + int(qty)
            medicine.save()

        varToPass = {
            'objects': objects,
            'total': total,
            'customer_name': customer_name,
            'customer_tel': customer_tel,
            'pharmacy_value': pharmacy_value
        }
        return render(request, 'advanced/page_receipt.html', varToPass)
    return redirect('sales:records')


@login_required(login_url='')
def records(request):
    sales_records = list(Records.objects.filter(owner=request.user.work_for).order_by('-invoice')) 
    print(sales_records)
    return render(request, 'advanced/page_sales_records.html', {'sales_records': sales_records})


@login_required(login_url='')
def sell(request):
    return render(request, 'advanced/page_sell.html')
    