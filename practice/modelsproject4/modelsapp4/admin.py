from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.Drinks)
admin.site.register(models.Menu)
admin.site.register(models.MenuCategory)