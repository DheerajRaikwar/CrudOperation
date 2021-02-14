from django.db import models

# Create your models here.

class User(models.Model):
    no = models.IntegerField()
    name = models.CharField(max_length=70)
    email = models.EmailField(max_length=100)
    Dob = models.DateField()
    city = models.CharField(max_length=60)
    password = models.CharField(max_length=20)
    