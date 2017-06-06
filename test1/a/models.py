from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=40)
    email = models.EmailField(max_length=40, unique=True)