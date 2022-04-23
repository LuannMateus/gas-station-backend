from django.db import models


class Tank(models.Model):
    type = models.CharField(max_length=120)
    maxCapacity = models.IntegerField()
    currentFuel = models.IntegerField()
