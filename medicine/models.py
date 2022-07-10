from unittest import result
from settings.models import Pharmacy
from userAuth.models import pmsUser
from django.db import models
from datetime import date


class Category(models.Model):
    name = models.CharField(max_length=30)
    image = models.ImageField(upload_to='uploads/', default='default')
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    in_pharmacy = models.ForeignKey(Pharmacy, db_column='in_pharmacy', on_delete=models.CASCADE)
    owner = models.ForeignKey(pmsUser, db_column='owner', on_delete=models.CASCADE)

    # class Meta:
    #      ordering = ['-date_modified']


class Stock(models.Model):
    name = models.CharField(max_length=30)
    generic_name = models.CharField(max_length=30, blank=True)
    category_name = models.ForeignKey(Category, db_column='category', on_delete=models.CASCADE)
    quantity = models.IntegerField()
    packaging = models.CharField(max_length=20)
    cost = models.IntegerField()
    price = models.IntegerField()
    best_before = models.DateField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    in_pharmacy = models.ForeignKey(Pharmacy, db_column='in_pharmacy', on_delete=models.CASCADE)
    owner = models.ForeignKey(pmsUser, db_column='owner', on_delete=models.CASCADE)
    sold = models.IntegerField(default=0)

    def is_exipired_medicine(self):
        return (date.today() - self.best_before).days > 1

    def is_medicine_available(self):
        return self.quantity > 1

