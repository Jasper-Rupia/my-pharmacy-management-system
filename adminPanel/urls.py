from django.urls import path
from . import views

urlpatterns = [
    path('a', views.index),
    path('category', views.category),
    path('pharmacy', views.pharmacy),
    path('profile', views.profile),
    path('receipt', views.receipt),
    path('sales_records', views.sales_records),
    path('sell', views.sell),
    path('stock', views.stock),
    path('users', views.users),
]
