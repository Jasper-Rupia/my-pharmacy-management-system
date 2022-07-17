
from django.db import models
from django.contrib.auth.models import AbstractUser


class pmsUser(AbstractUser):
    avata = models.ImageField(upload_to='users_dp/')
    tel = models.CharField(max_length=30, blank=True)
    title = models.CharField(max_length=30, blank=True)
    work_for = models.ForeignKey('self', db_column='work_for', on_delete=models.CASCADE, null=True, blank=True) 

 


 
#from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# class UserManager(BaseUserManager):
#     def create_user(self, email, name, password):
#         if not email:
#             raise ValueError('email is req') 
#         user=self.model(
#             email=self.normalize_email(email),
#             name=name,
#             password=password
#         )
#         user.set_password(password) #hashing
#         user.save(using=self._db)
#         return user

#     def create_superuser(self, email, name, password):
#         user=self.create_user( #call create user
#             email=email,
#             name=name,
#             password=password
#         )
#         user.save(using=self._db)
#         return user


# class User(AbstractBaseUser):
#     avata = models.ImageField(upload_to='uploads/', default='default_dp')
#     name = models.CharField(max_length=30)
#     email = models.CharField(unique=True, blank=False, max_length=30)
#     password = models.CharField(max_length=30, default='123')
#     tel = models.CharField(max_length=30, blank=True)
#     #role = models.CharField(max_length=30)
#     title = models.CharField(max_length=30, null=False, blank=False)
#     #work_for = models.CharField(max_length=30)
#     registerd_date = models.DateField(auto_now=True)
#     last_login = models.DateTimeField(auto_now=True)

#     USERNAME_FIELD = 'email'

#     REQUIRED_FIELDS = ['name']

#     objects = UserManager()