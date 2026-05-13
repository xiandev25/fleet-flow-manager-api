from django.db import models
from django.conf import settings
from django.core.exceptions import ValidationError

class Family(models.Model):
    primary_guardian = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="primary_families",
    )
    secondary_guardian = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="secondary_families",
    )
    family_registration_number = models.CharField(max_length=9)
    billing_address = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Family of {self.primary_guardian.get_full_name() or self.primary_guardian.username}"

    class Meta:
        verbose_name_plural = "Families"


class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    student_registration_number = models.CharField(max_length=11)
    family = models.ForeignKey(
        Family, on_delete=models.CASCADE, related_name="children"
    )
    assigned_line = models.ForeignKey(
        'routes.BusLine', 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True,
        related_name='enrolled_students'
    )
    assigned_stop = models.ForeignKey(
        'routes.BusStop', 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True,
        related_name='enrolled_students'
    )
    assigned_shuttle = models.ForeignKey(
        'routes.Shuttle',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='enrolled_students'
    )
    date_of_birth = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def clean(self):
        # 1. Check if both Shuttle and Bus Line/Stop are assigned
        if (self.assigned_line or self.assigned_stop) and self.assigned_shuttle:
            raise ValidationError("A student cannot be assigned to both a Bus Line and a Shuttle.")

        # 2. Ensure that if a line is assigned, a stop is also assigned
        if self.assigned_line and not self.assigned_stop:
            raise ValidationError("Please select a specific stop for the assigned Bus Line.")
            
        # 3. Ensure the stop belongs to the correct line
        if self.assigned_line and self.assigned_stop:
            if self.assigned_stop.line != self.assigned_line:
                raise ValidationError("The selected stop does not belong to the selected Bus Line.")

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
