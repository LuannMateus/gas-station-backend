from app.views import TankViewSet

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', TankViewSet)
urlpatterns = router.urls
