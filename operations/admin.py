from django.contrib import admin
from .models import TripAssignment

@admin.register(TripAssignment)
class TripAssignmentAdmin(admin.ModelAdmin):
    list_display = ('get_route', 'vehicle', 'driver', 'date', 'time_slot', 'status')
    list_filter = ('date', 'time_slot', 'status')
    search_fields = ('vehicle__license_plate', 'driver__username', 'bus_line__name', 'shuttle__name')

    def get_route(self, obj):
        return obj.bus_line.name if obj.bus_line else obj.shuttle.name
    get_route.short_description = 'Route'
