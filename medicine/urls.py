from django.urls import path
from . import views

urlpatterns = [
    path('category', views.category, name='category'),
    path('addCategory', views.addCategory),
    path('delCategory', views.delCategory),
    path('stock', views.stock, name='stock'),
    path('addStock', views.addStock),
    path('delStock', views.delStock),
]
