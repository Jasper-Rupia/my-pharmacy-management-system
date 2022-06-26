from django.urls import path
from . import views

urlpatterns = [
    path('login', views.user_login, name='log'),
    path('logout', views.user_logout),
    path('newPassword', views.newPassword),
    path('recover', views.recover),
    path('register', views.register, name='register'),
]
