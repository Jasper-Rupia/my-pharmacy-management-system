from django.urls import path
from . import views


app_name = 'settings'
urlpatterns = [
    path('pharmacy', views.pharmacy, name='pharmacy'),
    path('addPharmacy', views.addPharmacy),
    path('delPharmacy/<int:id>', views.delPharmacy),
    path('updPharmacy', views.updPharmacy),
    
    path('profile', views.profile, name='profile'),
    path('updateDp', views.updateDp),
    path('updProfile', views.updProfile),
    path('updPassword', views.updPassword),

    path('users', views.users, name='users'),
    path('addUsers', views.addUsers),
    path('delUsers', views.delUsers),
]
