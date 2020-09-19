from django.db import models

# Create your models here.
class Account(models.Model):
    ID = models.CharField(max_length=15, primary_key=True)
    password = models.CharField(max_length=15)
    isManager = models.BooleanField(default=False)


class User(models.Model):
    account = models.OneToOneField(Account, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=20)
    birthday = models.DateField()
    isMale = models.BooleanField(default=True)
    college = models.CharField(max_length=30)
    address = models.CharField(max_length=50)


class Teacher(models.Model):
    account = models.OneToOneField(Account, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=20)
    isMale = models.BooleanField(default=True)


class Commodity(models.Model):
    ID = models.ForeignKey(Account, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    description = models.CharField(max_length=250)
    owner = models.CharField(max_length=15)


