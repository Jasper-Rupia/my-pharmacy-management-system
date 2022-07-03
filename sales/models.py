from django.db import models
from django.contrib.auth.models import User


class Records(models.Model):
    invoice = models.CharField(max_length=30)
    customer = models.CharField(max_length=30)
    contact = models.CharField(max_length=30)
    items = models.IntegerField()
    total_amount = models.IntegerField()
    trans_by = models.ForeignKey(User, db_column='tran_by', on_delete=models.DO_NOTHING)
    trans_date = models.DateField(auto_now=True)

