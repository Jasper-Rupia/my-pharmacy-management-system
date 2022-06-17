from django.urls import path
from . import views

urlpatterns = [
    path('login', views.index),
    path('newPassword', views.newPassword),
    path('recover', views.recover),
    path('register', views.register),
]
