from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import VehicleViewSet, MaintenanceLogViewSet

router = DefaultRouter()
router.register(r'vehicles', VehicleViewSet)
router.register(r'maintenance', MaintenanceLogViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
