from django.db import models
from django.contrib.auth.models import User


class Pharmacy(models.Model):
    name = models.CharField(max_length=30)
    location = models.TextField(max_length=100)
    owner = models.ForeignKey(User, db_column='owner', on_delete=models.CASCADE)
    registerd_date = models.DateTimeField(auto_now=True)

