from django.db import models
from django.db.models.fields import BooleanField

# Create your models here.

class user(models.Model):
    thandaperu = models.BigIntegerField()
    name = models.CharField(max_length=100)
    city = models.TextField()
    street = models.CharField(max_length=100)
    premises = models.CharField(max_length=100)
    pincode = models.BigIntegerField()
    phonenumber = models.BigIntegerField()
    adhaar = models.BigIntegerField()
    landBefore = models.CharField(max_length=100)
    landAfter = models.CharField(max_length=100)
    thalukVerification = models.CharField(max_length=100)
    villageVerification = models.CharField(max_length=100)
    notification = BooleanField(default=False)

class thaluk(models.Model):
    name = models.CharField(max_length=100)
    phonenumber = models.BigIntegerField()
    place = models.CharField(max_length=100)
    pincode = models.BigIntegerField()
    adhaar = models.BigIntegerField()
    password = models.TextField()

class village(models.Model):
    name = models.CharField(max_length=100)
    phonenumber = models.BigIntegerField()
    place = models.CharField(max_length=100)
    pincode = models.BigIntegerField()
    adhaar = models.BigIntegerField()
    password = models.TextField()