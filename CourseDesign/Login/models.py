from django.db import models

# Create your models here.
class UserAccount(models.Model):
    userAccount = models.CharField(max_length=15, primary_key=True)
    userPassword = models.CharField(max_length=15)

    def __str__(self):
        return self.userAccount
