from app.models import Tank

from rest_framework import serializers


class TankSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tank
        fields = ['id', 'type', 'maxCapacity', 'currentFuel']
