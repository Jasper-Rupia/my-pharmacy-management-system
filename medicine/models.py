from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=30)


class Stock(models.Model):
    name = models.CharField(max_length=30)
    generic_name = models.CharField(max_length=30)
    category_name = models.ForeignKey('Category', on_delete=models.CASCADE)
    packaging = models.IntegerField()
    quantity = models.CharField(max_length=5)
    cost = models.IntegerField()
    price = models.IntegerField()
    best_before = models.DateField()
    status = models.CharField(max_length=12)
