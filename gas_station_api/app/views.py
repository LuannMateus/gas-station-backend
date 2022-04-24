from app.models import Tank, FuelPump, Fill
from app.serializers import TankSerializer, FuelPumpSerializer, FillSerializer

from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import NotFound, ValidationError


class TankListAndCreateView(APIView):
    def get(self, request):
        tanks = Tank.objects.all()
        serializer = TankSerializer(tanks, many=True)

        return Response(serializer.data)

    def post(self, request):
        serializer = TankSerializer(data=request.data)

        if request.data['currentFuel'] > request.data['maxCapacity']:
            raise ValidationError(
                {"currentFuel":  "Current fuel cannot be greater than max capacity"}, status.HTTP_400_BAD_REQUEST)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TankDetailChangeAndDeleteView(APIView):
    def get_object(self, pk):
        try:
            return Tank.objects.get(pk=pk)
        except Tank.DoesNotExist:
            raise NotFound()

    def get(self, request, pk):
        tank = self.get_object(pk)
        serializer = TankSerializer(tank)

        return Response(serializer.data)

    def put(self, request, pk):
        tank = self.get_object(pk)

        if request.data['currentFuel'] > request.data['maxCapacity']:
            raise ValidationError(
                {"currentFuel":  "Current fuel cannot be greater than max capacity"}, status.HTTP_400_BAD_REQUEST)

        serializer = TankSerializer(tank, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        tank = self.get_object(pk)

        tank.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


class FuelPumpListAndCreateView(APIView):
    def get(self, request):
        fuelPumps = FuelPump.objects.all()
        serializer = FuelPumpSerializer(fuelPumps, many=True)

        return Response(serializer.data)

    def post(self, request):
        serializer = FuelPumpSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FuelPumpDetailChangeAndDeleteView(APIView):
    def get_object(self, pk):
        try:
            return FuelPump.objects.get(pk=pk)
        except FuelPump.DoesNotExist:
            raise NotFound()

    def get(self, request, pk):
        fuelPump = self.get_object(pk)
        serializer = FuelPumpSerializer(fuelPump)

        return Response(serializer.data)

    def put(self, request, pk):
        fuelPump = self.get_object(pk)

        serializer = FuelPumpSerializer(fuelPump, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        fuelPump = self.get_object(pk)

        fuelPump.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


class FillListAndCreateView(APIView):
    def get(self, request):
        fills = Fill.objects.all()
        serializer = FillSerializer(fills, many=True)

        return Response(serializer.data)

    def post(self, request):
        pumpId = request.data.get('pump')
        amount = request.data.get('amount')

        pump = FuelPump.objects.get(pk=pumpId)

        pricePerLiter = pump.pricePerLiter

        quantityLiters = Fill.get_quantityLiters(amount, pricePerLiter)

        request.data['quantityLiters'] = quantityLiters
        request.data['taxPaid'] = Fill.get_taxPaid(amount)

        serializer = FillSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FillDetailChangeAndDeleteView(APIView):
    def get_object(self, pk):
        try:
            return Fill.objects.get(pk=pk)
        except Fill.DoesNotExist:
            raise NotFound()

    def get(self, request, pk):
        fill = self.get_object(pk)
        serializer = FillSerializer(fuelPump)

        return Response(serializer.data)

    def put(self, request, pk):
        fill = self.get_object(pk)

        amount = request.data.get('amount')
        pumpId = request.data.get('pump')

        if pumpId == None:
            raise ValidationError(
                {"pump": "Pump is required"}, status.HTTP_400_BAD_REQUEST)
        try:
            pump = FuelPump.objects.get(pk=pumpId)
        except FuelPump.DoesNotExist:
            raise NotFound(
                {"pump": "Pump with id {} does not exist".format(pumpId)},
                status.HTTP_404_NOT_FOUND)
        except Exception as e:
            raise ValidationError({
                "error": e
            })

        pricePerLiter = pump.pricePerLiter

        quantityLiters = Fill.get_quantityLiters(amount, pricePerLiter)

        request.data['quantityLiters'] = quantityLiters
        request.data['taxPaid'] = Fill.get_taxPaid(amount)

        serializer = FillSerializer(fill, data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        fill = self.get_object(pk)

        fill.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
