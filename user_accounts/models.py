from django.db import models

# Create your models here.
class User_Accounts(models.Model):
    email = models.EmailField(max_length=100,unique=True,primary_key=True)
    password = models.CharField(max_length=12)