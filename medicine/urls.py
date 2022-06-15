from django.urls import path
from . import views

urlpatterns = [
    path('category', views.category),
    path('stock', views.stock),
]
