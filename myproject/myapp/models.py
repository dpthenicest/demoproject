from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=40)
    email = models.EmailField(max_length=50)
    phone_no = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Menu(models.Model):
    name = models.CharField(max_length=100)
    cuisine = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    size = models.CharField(max_length=1, default='M')
    person = models.ForeignKey(Person, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.name}: {self.cuisine}"
