from django.urls import path
from . import views

urlpatterns = [
    path('receipt', views.receipt),
    path('sales_records', views.sales_records),
    path('sell', views.sell),
]
