from django.urls import path
from . import views

urlpatterns = [
    path('category', views.category, name='category'),
    path('stock', views.stock, name='stock'),
    path('addCategory', views.addCategory),
    path('delCategory', views.delCategory),
]
