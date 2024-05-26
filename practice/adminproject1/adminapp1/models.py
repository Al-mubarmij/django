from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    summary = models.CharField(max_length=300)
    blog = models.CharField(max_length=5000)