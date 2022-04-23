from app.views import TankViewSet, FuelPumpViewSet

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'tanks', viewset=TankViewSet)
router.register(r'fuelPumps', viewset=FuelPumpViewSet)
urlpatterns = router.urls
