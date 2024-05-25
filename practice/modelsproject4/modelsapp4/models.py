from django.db import models

# Create your models here.
class Drinks(models.Model):
    drink = models.CharField(max_length=200, default='lemon')
    price = models.IntegerField(default=0)
    

class MenuCategory(models.Model):
    menu_category_name = models.CharField(max_length=200)

class Menu(models.Model):
    menu_item = models.CharField(max_length=200)
    price = models.IntegerField()
    category_id = models.ForeignKey(MenuCategory, on_delete=models.PROTECT, default=None)