from distutils.command.upload import upload
from email.mime import image
from email.policy import default
from django.db import models



class Category(models.Model):
    name = models.CharField(primary_key=True, max_length=30)
    image = models.ImageField(upload_to='uploads/', default='default')
    date_created = models.DateTimeField(auto_now=True)


class Stock(models.Model):
    name = models.CharField(primary_key=True, max_length=30)
    generic_name = models.CharField(max_length=30, blank=True)
    category_name = models.ForeignKey('Category', db_column='category', on_delete=models.CASCADE)
    quantity = models.IntegerField()
    packaging = models.CharField(max_length=20)
    cost = models.IntegerField()
    price = models.IntegerField()
    best_before = models.DateField()
    date_created = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=30, default='Available')
    