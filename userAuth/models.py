# from django.db import models


# class pharmacy(models.Model):
#     invoice = models.CharField(max_length=30)


# class users(models.Model):
#     #avata = models.FileField(upload_to='uploads/')
#     name = models.CharField(max_length=30)
#     email = models.EmailField(max_length=30)
#     tel = models.CharField(max_length=15)
#     role = models.CharField(max_length=10)
#     registerd_date = models.DateField()
#     ACTIVE = 'active'
#     INACTIVE = 'blocked'
#     operation_status = [
#         (ACTIVE, 'ACTIVE'),
#         (INACTIVE, 'INACTIVE'),
#     ]
#     operate = models.CharField(
#         max_length=7,
#         choices=operation_status,
#         default=ACTIVE,
#     )


