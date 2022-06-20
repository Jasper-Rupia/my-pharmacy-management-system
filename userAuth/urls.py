from django.urls import path
from . import views

urlpatterns = [
    path('login', views.login, name='login'),
    path('newPassword', views.newPassword),
    path('recover', views.recover),
    path('register', views.register),
]
