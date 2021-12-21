from django.db import models

# Create your models here.

class Wallet(models.Model):
    user = models.ForeignKey('users.Users')
    balance = models.IntegerField()
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title