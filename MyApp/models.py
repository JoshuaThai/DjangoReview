from django.db import models

# Create your models here.
class Ticket(models.Model):
    week = models.CharField(max_length=14)
    date_time = models.DateTimeField()
    location = models.CharField(max_length=100)
