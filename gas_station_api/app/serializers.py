from app.models import Tank, FuelPump

from rest_framework import serializers


class TankSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tank
        fields = ['id', 'type', 'maxCapacity', 'currentFuel']


class FuelPumpSerializer(serializers.ModelSerializer):
    class Meta:
        model = FuelPump
        fields = ['id', 'type', 'pricePerLiter', 'tankId']
