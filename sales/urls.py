from django.urls import path
from . import views

urlpatterns = [
    path('receipt', views.receipt),
    path('records', views.records),
    path('sell', views.sell),
]
