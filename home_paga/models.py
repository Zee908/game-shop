from django.db import models
from django.contrib.auth.models import AbstractUser,AbstractBaseUser 
# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=150)
    price = models.DecimalField(max_digits=20)
    description = models.CharField(max_length=150)
    category = models.CharField(max_length=150)
    game_id= models.CharField(max_length=150)
    genre= models.CharField(max_length=150)
    tags= models.CharField(max_length=150)

