from django.urls import path
from . import views

urlpatterns = [
    # path('', views.login, name='signin'),
    # path('logout', views.logout),
    path('', views.user_login, name='signin'),
    path('logout', views.user_logout),
    path('newPassword', views.newPassword),
    path('recover', views.recover),
    path('register', views.register, name='register'),
    path('registerUser', views.registerUser),
]
