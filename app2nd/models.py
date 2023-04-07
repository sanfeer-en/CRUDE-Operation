from django.db import models

# Create your models here.
class UserDetails(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    city = models.CharField(max_length=100)
    pincode =models.CharField(max_length=10)
    message = models.TextField(max_length=400)
    password = models.CharField(max_length=10)
    
    
    