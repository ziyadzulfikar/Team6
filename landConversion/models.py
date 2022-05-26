from django.db import models

# Create your models here.

class user(models.Model):
    name = models.CharField(max_length=100)
    city = models.TextField()
    street = models.CharField(max_length=100)
    premises = models.CharField(max_length=100)
    pincode = models.IntegerField()
    phonenumber = models.IntegerField()
    adhaar = models.IntegerField()
    thandaperu = models.IntegerField()