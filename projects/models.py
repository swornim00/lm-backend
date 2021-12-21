from django.db import models
from django.db.models.base import Model

# Create your models here.

class Project(models.Model):
    client = models.ForeignKey('users.Users')
    freelancer = models.ForeignKey('users.Users')
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title