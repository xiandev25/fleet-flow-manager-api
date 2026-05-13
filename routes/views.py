from rest_framework import viewsets
from .models import BusLine, BusStop, Shuttle
from .serializers import BusLineSerializer, BusStopSerializer, ShuttleSerializer
from users.permissions import IsManager, IsDriver

class BusLineViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing Bus Lines.
    Full access for Managers/Admins. Viewing for Drivers.
    """
    queryset = BusLine.objects.all()
    serializer_class = BusLineSerializer
    permission_classes = [IsDriver] # Drivers need to see the routes

class BusStopViewSet(viewsets.ModelViewSet):
    queryset = BusStop.objects.all()
    serializer_class = BusStopSerializer
    permission_classes = [IsDriver]

class ShuttleViewSet(viewsets.ModelViewSet):
    queryset = Shuttle.objects.all()
    serializer_class = ShuttleSerializer
    permission_classes = [IsDriver]
