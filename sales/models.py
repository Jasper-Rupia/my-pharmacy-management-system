from django.db import models
from userAuth.models import pmsUser
from settings.models import Pharmacy


class Records(models.Model):
    invoice = models.CharField(max_length=30)
    customer = models.CharField(max_length=30)
    contact = models.CharField(max_length=30)
    items = models.IntegerField()
    total_amount = models.IntegerField()
    trans_by = models.ForeignKey(pmsUser, db_column='tran_by', related_name='tran_by', on_delete=models.DO_NOTHING)
    trans_date = models.DateField(auto_now=True)
    in_pharmacy = models.ForeignKey(Pharmacy, db_column='in_pharmacy', on_delete=models.CASCADE)
    owner = models.ForeignKey(pmsUser, db_column='owner', related_name='owner', on_delete=models.DO_NOTHING)

