from django.db import models
from userAuth.models import pmsUser


class Pharmacy(models.Model):
    name = models.CharField(max_length=30)
    location = models.TextField(max_length=100)
    owner = models.OneToOneField(pmsUser, db_column='owner', on_delete=models.CASCADE, null=True, blank=True)
    registerd_date = models.DateTimeField(auto_now_add=True)

