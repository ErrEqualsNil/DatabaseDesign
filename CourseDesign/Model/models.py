from django.db import models

# Create your models here.


class User(models.Model):
    id = models.CharField(max_length=18, primary_key=True)
    password = models.CharField(max_length=18)
    name = models.CharField(max_length=20)
    birthday = models.DateField()
    isMale = models.BooleanField(default=True)
    college = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    QQ = models.CharField(max_length=20)
    tel = models.CharField(max_length=20)
    email = models.CharField(max_length=30)


class Teacher(models.Model):
    id = models.CharField(max_length=18, primary_key=True)
    password = models.CharField(max_length=18)
    name = models.CharField(max_length=20)
    isMale = models.BooleanField(default=True)


class Commodity(models.Model):
    name = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    description = models.CharField(max_length=250)
    owner = models.CharField(max_length=15)
    status = models.BooleanField(default=True)
    image = models.CharField(max_length=30)


class Transaction(models.Model):
    buyer = models.CharField(max_length=18)
    seller = models.CharField(max_length=18)
    commodity = models.ForeignKey(Commodity, on_delete=models.DO_NOTHING)
    status = models.IntegerField()
    comment = models.CharField(max_length=200)

