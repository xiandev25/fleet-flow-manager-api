from django.db import models
from django.conf import settings


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


class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    student_registration_number = models.CharField(max_length=11)
    family = models.ForeignKey(
        Family, on_delete=models.CASCADE, related_name="children"
    )
    date_of_birth = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
