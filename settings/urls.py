from django.urls import path
from . import views

urlpatterns = [
    path('pharmacy', views.pharmacy),
    path('profile', views.profile),
    path('users', views.users),
]
