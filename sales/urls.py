from django.urls import path
from . import views


app_name = 'sales'
urlpatterns = [
    path('receipt', views.receipt),
    path('records', views.records),
    path('sell', views.sell),
]
