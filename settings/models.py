from django.db import models
from pkg_resources import working_set


class Pharmacy(models.Model):
    name = models.CharField(max_length=30)
    location = models.TextField(max_length=100)
    #owner = models.ForeignKey('User', db_column='owner', on_delete=models.CASCADE)
    owner = models.CharField(max_length=30, default='user')
    registerd_date = models.DateTimeField(auto_now=True)


class User(models.Model):
    avata = models.ImageField(upload_to='uploads/', default='default_dp')
    name = models.CharField(max_length=30)
    email = models.CharField(unique=True, blank=False, max_length=30)
    password = models.CharField(max_length=30, default='123')
    tel = models.CharField(max_length=30, blank=True)
    #role = models.CharField(max_length=30)
    title = models.CharField(max_length=30, null=False, blank=False)
    #work_for = models.CharField(max_length=30)
    registerd_date = models.DateField(auto_now=True)
