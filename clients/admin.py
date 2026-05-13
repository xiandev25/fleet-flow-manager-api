from django.contrib import admin
from .models import Family, Student

@admin.register(Family)
class FamilyAdmin(admin.ModelAdmin):
    list_display = ('primary_guardian', 'family_registration_number', 'created_at')
    search_fields = ('primary_guardian__username', 'family_registration_number')

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'student_registration_number', 'family')
    search_fields = ('first_name', 'last_name', 'student_registration_number')
    list_filter = ('assigned_line', 'assigned_shuttle')
