from rest_framework import serializers
from .models import TripAssignment

class TripAssignmentSerializer(serializers.ModelSerializer):
    driver_name = serializers.CharField(source='driver.get_full_name', read_only=True)
    vehicle_plate = serializers.CharField(source='vehicle.license_plate', read_only=True)
    route_name = serializers.SerializerMethodField()
    status_display = serializers.CharField(source='get_status_display', read_only=True)

    class Meta:
        model = TripAssignment
        fields = [
            'id', 'vehicle', 'vehicle_plate', 'driver', 'driver_name',
            'bus_line', 'shuttle', 'route_name', 'date', 'time_slot', 
            'status', 'status_display', 'notes', 'created_at'
        ]

    def get_route_name(self, obj):
        if obj.bus_line:
            return f"Line: {obj.bus_line.name}"
        if obj.shuttle:
            return f"Shuttle: {obj.shuttle.name}"
        return "Unknown Route"
