from django.db import models
from django.db.models.deletion import SET_NULL
from django.db.models.enums import Choices
from django.db.models.fields import CharField

# Create your models here.

class Company(models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=50)
    found_year = models.DateField()

    def __str__(self):
        return self.name


class Shoes(models.Model):
    TYPE_CHOICES = [
        ("UNIVERSALL" , "UNIVERSALL"),
        ("KIDS" , "KIDS"),
        ("MAN" , "MAN"),
        ("WOMEN", "WOMEN")
    ]
    title = models.CharField(max_length=50)
    brand_name = models.ForeignKey(Company, on_delete=SET_NULL, blank=True, null=True)
    type_choices = models.CharField(max_length=11, choices=TYPE_CHOICES, default="UNIVERSALL")
    price = models.PositiveIntegerField()
    image = models.ImageField(upload_to="images/")

    def __str__(self):
        return self.title

class Contact(models.Model):
    name = models.CharField(max_length=100)
    phone = models.PositiveIntegerField()
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name