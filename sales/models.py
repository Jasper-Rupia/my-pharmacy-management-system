from django.db import models
from settings.models import User

class Records(models.Model):
    invoice = models.CharField(max_length=30)
    customer = models.CharField(max_length=30)
    contact = models.CharField(max_length=30)
    items = models.IntegerField()
    amount = models.IntegerField()
    #trans_by = models.ForeignKey('users', db_column='tran_by', on_delete=models.CASCADE)
    trans_by = models.CharField(max_length=30)
    trans_date = models.DateField(auto_now=True)
