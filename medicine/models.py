from settings.models import Pharmacy
from django.db import models


class Category(models.Model):
    name = models.CharField(unique=True, max_length=30)
    image = models.ImageField(upload_to='uploads/', default='default')
    date_created = models.DateTimeField(auto_now=True)
    in_pharmacy = models.ForeignKey(Pharmacy,db_column='in_pharmacy', on_delete=models.CASCADE)


class Stock(models.Model):
    name = models.CharField(unique=True, max_length=30)
    generic_name = models.CharField(max_length=30, blank=True)
    category_name = models.ForeignKey(Category, db_column='category', on_delete=models.CASCADE)
    quantity = models.IntegerField()
    packaging = models.CharField(max_length=20)
    cost = models.IntegerField()
    price = models.IntegerField()
    best_before = models.DateField()
    date_created = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=30, default='Available')
    