from django.db import models

# Create your models here.
class House(models.Model):
    number = models.CharField(max_length=15)
    location = models.CharField(max_length=32) 
    price = models.IntegerField(default=0)
    size = models.IntegerField(default=1)
    description = models.TextField()
    action = models.CharField(max_length=16)
    posted = models.DateTimeField(auto_now_add=True)

class Car(models.Model): 
    number = models.CharField(max_length=15) 
    ctype = models.CharField(max_length=32) 
    price = models.IntegerField(default=0)
    description = models.TextField() 
    action = models.CharField(max_length=16)
    posted = models.DateTimeField(auto_now_add=True) 

class Deal(models.Model):
    number = models.CharField(max_length=16) 
    name = models.CharField(max_length=32) 
    price = models.IntegerField(default=0) 
    description = models.TextField() 
    action = models.CharField(max_length=16) 
    posted= models.DateTimeField(auto_now_add=True)

class Log(models.Model):
    number = models.CharField(max_length=16) 
    error = models.CharField(max_length=64) 
    endpoint = models.CharField(max_length=16) 
    created = models.DateTimeField(auto_now_add=True) 
    


    
    
