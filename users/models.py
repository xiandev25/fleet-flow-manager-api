from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    class Role(models.TextChoices):
        ADMIN = 'ADMIN', 'Admin'
        MANAGER = 'MANAGER', 'Manager'
        DRIVER = 'DRIVER', 'Driver'
        MECHANIC = 'MECHANIC', 'Mechanic'
        GUARDIAN = 'GUARDIAN', 'Guardian'

    role = models.CharField(
        max_length=10,
        choices=Role.choices,
        default=Role.GUARDIAN
    )
    phone_number = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return f"{self.username} ({self.get_role_display()})"
