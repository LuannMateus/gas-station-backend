from app.models import Tank, FuelPump
from app.serializers import TankSerializer, FuelPumpSerializer

from rest_framework import viewsets


class TankViewSet(viewsets.ModelViewSet):
    queryset = Tank.objects.all()
    serializer_class = TankSerializer


class FuelPumpViewSet(viewsets.ModelViewSet):
    queryset = FuelPump.objects.all()
    serializer_class = FuelPumpSerializer
