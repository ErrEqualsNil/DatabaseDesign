from django.db import models

# Create your models here.
class Account(models.Model):
    ID = models.CharField(max_length=15, primary_key=True)
    password = models.CharField(max_length=15)
    isManager = models.BooleanField(default=False)

class User(models.Model):
    account = models.OneToOneField(Account, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=20)
    birthday = models.DateField(auto_now_add=True)
    isMale = models.BooleanField(default=True)
    college = models.CharField(max_length=30)
    address = models.CharField(max_length=50)


