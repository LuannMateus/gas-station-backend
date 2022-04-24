import app.views as views
from django.urls import path


urlpatterns = [
    path(r'tanks/', views.TankListAndCreateView.as_view()),
    path(r'tanks/<str:pk>/', views.TankDetailChangeAndDeleteView.as_view()),
    path(r'fuelPumps/', views.FuelPumpListAndCreateView.as_view()),
    path(r'fuelPumps/<str:pk>/', views.FuelPumpDetailChangeAndDeleteView.as_view()),
    path(r'fills/', views.FillListAndCreateView.as_view()),
    path(r'fills/<str:pk>/', views.FillDetailChangeAndDeleteView.as_view()),
]
