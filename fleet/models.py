from django.db import models
from django.conf import settings

# Create your models here.


class Vehicle(models.Model):
    class Status(models.TextChoices):
        AVAILABLE = "AVAILABLE", "Available"
        IN_USE = "IN_USE", "In Use"
        IN_MAINTENANCE = "IN_MAINTENANCE", "In Maintenance"
        IN_REPAIR = "IN_REPAIR", "In Repair"
        REFUELLING = "REFUELLING", "Refuelling"
        SPECIAL_ASSIGNMENT = "SPECIAL_ASSIGNMENT", "Special Assignment"
        RETIRED = "RETIRED", "Retired"

    license_plate = models.CharField(max_length=20, unique=True)
    immatriculation_number = models.CharField(
        max_length=17, unique=True, blank=True, null=True
    )
    brand = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    manufacture_year = models.PositiveIntegerField()
    status = models.CharField(
        max_length=20, choices=Status.choices, default=Status.AVAILABLE
    )
    current_mileage = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.brand} {self.model} ({self.license_plate})"


class MaintenanceLog(models.Model):
    class JobType(models.TextChoices):
        MAINTENANCE = "MAINTENANCE", "Routine Maintenance"
        REPAIR = "REPAIR", "Repair"

    vehicle = models.ForeignKey(
        Vehicle, on_delete=models.CASCADE, related_name="maintenance_logs"
    )
    mechanic = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="maintenance_jobs",
    )
    job_type = models.CharField(
        max_length=20,
        choices=JobType.choices,
        default=JobType.MAINTENANCE,
    )
    action_taken = models.TextField()
    completion_date = models.DateField()
    next_service_mileage = models.PositiveIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Maintenance for {self.vehicle} on {self.completion_date}"
