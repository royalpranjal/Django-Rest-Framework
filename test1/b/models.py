from django.db import models

class Animal(models.Model):
    name = models.CharField(max_length=100, unique=True)
    type = models.CharField(max_length=100)