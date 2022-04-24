from rest_framework.exceptions import ValidationError
from rest_framework.status import HTTP_400_BAD_REQUEST


class CreateFillUp:
    def __init__(self, tankRepository, fuelPumpRepository, fillRepository):
        self.fuelPumpRepository = fuelPumpRepository
        self.fillRepository = fillRepository
        self.tankRepository = tankRepository

    def execute(self, pumpId: str, amount: float):
        data = {'quantityLiters': '', 'taxPaid': ''}

        pump = self.fuelPumpRepository.objects.get(pk=pumpId)

        pricePerLiter = pump.pricePerLiter

        quantityLiters = self.fillRepository.get_quantityLiters(
            amount, pricePerLiter)

        data['quantityLiters'] = quantityLiters
        data['taxPaid'] = self.fillRepository.get_taxPaid(amount)

        tank = self.tankRepository.objects.get(
            pk=pump.tank.id)

        if tank.currentFuel - data['quantityLiters'] < 0:
            raise ValidationError(
                {"error": "Not enough gas"}, HTTP_400_BAD_REQUEST
            )

        return data
