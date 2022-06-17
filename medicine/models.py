from distutils.command.upload import upload
from email.mime import image
from email.policy import default
from django.db import models



class Category(models.Model):
    name = models.CharField(primary_key=True, max_length=20)
    image = models.ImageField(upload_to='uploads/', default='no_medicine_image')


class Stock(models.Model):
    name = models.CharField(primary_key=True, max_length=20)
    generic_name = models.CharField(max_length=20)
    category_name = models.ForeignKey('Category', on_delete=models.CASCADE)
    packaging = models.IntegerField()
    quantity = models.IntegerField()
    cost = models.IntegerField()
    price = models.IntegerField()
    best_before = models.DateField()
    status = models.CharField(max_length=12, default='Available')
    