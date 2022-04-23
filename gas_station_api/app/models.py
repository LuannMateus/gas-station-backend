from django.db import models
import uuid as uuid_lib


class Tank(models.Model):
    id = models.UUIDField(
        default=uuid_lib.uuid4(),
        unique=True,
        primary_key=True,
        editable=False
    )
    type = models.CharField(max_length=120)
    maxCapacity = models.IntegerField()
    currentFuel = models.IntegerField()


class FuelPump(models.Model):
    id = models.UUIDField(
        default=uuid_lib.uuid4(),
        unique=True,
        primary_key=True,
        editable=False
    )
    type = models.CharField(max_length=120)
    pricePerLiter = models.FloatField()
    tankId = models.ForeignKey(Tank, on_delete=models.PROTECT)
