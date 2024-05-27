from django.db import models

# Create your models here.
class Message(models.Model):
    message = models.CharField(max_length=1000)
    sender = models.CharField(max_length=200)
    time_sent = models.TimeField(auto_now=True)