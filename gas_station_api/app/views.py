from app.models import Tank
from app.serializers import TankSerializer

from rest_framework import viewsets


class TankViewSet(viewsets.ModelViewSet):
    queryset = Tank.objects.all()
    serializer_class = TankSerializer
