from app.models import Tank, FuelPump, Fill

from rest_framework import serializers


class TankSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tank
        fields = ['id', 'type', 'maxCapacity', 'currentFuel']


class FuelPumpSerializer(serializers.ModelSerializer):
    class Meta:
        model = FuelPump
        fields = ['id', 'type', 'pricePerLiter', 'tank']


class FuelPumpWithTankSerializer(serializers.ModelSerializer):
    tank = TankSerializer(
        read_only=True

    )

    class Meta:
        model = FuelPump
        fields = ['id', 'type', 'pricePerLiter', 'tank']


class FillSerializer(serializers.ModelSerializer):

    class Meta:
        model = Fill
        fields = ['id', 'pump', 'amount',
                  'quantityLiters', 'taxPaid', 'fill_at']


class FillWithFuelPumpAndTankSerializer(serializers.ModelSerializer):
    pump = FuelPumpWithTankSerializer(
        read_only=True
    )

    class Meta:
        model = Fill
        fields = ['id', 'pump', 'amount',
                  'quantityLiters', 'taxPaid', 'fill_at']
