from django.db import models

# Create your models here.
class Drinks(models.Model):
    drink = models.CharField(max_length=200, default='lemon')
    price = models.IntegerField(default=0)
    