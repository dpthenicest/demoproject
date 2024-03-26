from unicodedata import name
from django.db import models

# Create your models here.

class Menu(models.Model):
  name = models.CharField(max_length=100)
  cuisine = models.CharField(max_length=100)
  price = models.IntegerField()
  size = models.CharField(max_length=1, default='M')

  def __str__(self):
    return self.name + ": " + self.cuisine
  
class Person(models.Model):
  name = models.CharField(max_length=40)
  email = models.EmailField(max_length=50)
  phone_no = models.IntegerField()