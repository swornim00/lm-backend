from django.db import models

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=20)
    middle_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    dob = models.DateField()
    email = models.EmailField()
    pan_number = models.IntegerField()
    registration_number = models.CharField(max_length=20)
    registration_document_type = models.CharField(max_length=20)
    created_on = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title