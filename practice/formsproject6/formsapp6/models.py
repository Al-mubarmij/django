from django.db import models

# Create your models here.
class Book(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    city = models.CharField(max_length=30)
    