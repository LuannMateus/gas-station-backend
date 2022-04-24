from django.db import models
import uuid as uuid_lib
from django.core.validators import MinValueValidator, MaxValueValidator


class Tank(models.Model):
    id = models.UUIDField(
        default=uuid_lib.uuid4,
        unique=True,
        primary_key=True,
        editable=False,
        auto_created=True
    )
    type = models.CharField(max_length=120)
    maxCapacity = models.FloatField(
        validators=[MinValueValidator(0.0), MaxValueValidator(30000)]
    )
    currentFuel = models.FloatField(
        validators=[MinValueValidator(0.0)]
    )


class FuelPump(models.Model):
    id = models.UUIDField(
        default=uuid_lib.uuid4,
        unique=True,
        primary_key=True,
        editable=False,
        auto_created=True
    )
    type = models.CharField(max_length=120)
    pricePerLiter = models.FloatField(
        validators=[MinValueValidator(0.0)]
    )
    tank = models.ForeignKey(Tank, on_delete=models.PROTECT)


class Fill(models.Model):

    id = models.UUIDField(
        default=uuid_lib.uuid4,
        unique=True,
        primary_key=True,
        editable=False,
        auto_created=True
    )
    pump = models.ForeignKey(FuelPump, on_delete=models.PROTECT)
    taxPaid = models.FloatField(
        auto_created=True, default=0, blank=True
    )
    quantityLiters = models.FloatField(
        auto_created=True, default=0, blank=True)
    amount = models.FloatField(
        validators=[MinValueValidator(1.0)]
    )
    fill_at = models.DateTimeField(auto_now_add=True)

    def get_taxPaid(amount: float):
        amountTax = amount * 0.13

        return amountTax

    def get_quantityLiters(amount: float, pricePerLiter: float):
        amountTax = Fill.get_taxPaid(amount)
        amountWithTax = amount - amountTax
        quantityLiters = amountWithTax / pricePerLiter

        return quantityLiters
