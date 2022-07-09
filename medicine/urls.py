from django.urls import path
from . import views

app_name = 'medicine'
urlpatterns = [
    path('category', views.category, name='category'),
    path('addCategory', views.addCategory),
    path('delCategory', views.delCategory),

    path('stock', views.stock, name='stock'),
    path('addStock', views.addStock),
    path('delSellStock', views.delSellStock),
    path('updStock', views.updStock),
    path('toUpdStock/<int:id>', views.toUpdStock),

    #path('fetchDataStock', views.fetchDataStock),
    #path('updStock', views.updStock),
]
