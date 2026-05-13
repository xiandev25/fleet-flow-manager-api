from rest_framework import permissions

class IsAdmin(permissions.BasePermission):
    """
    Allows access only to users with the 'ADMIN' role.
    """
    def has_permission(self, request, view):
        return (
            request.user.is_authenticated and 
            (request.user.role == 'ADMIN' or request.user.is_superuser)
        )

class IsManager(permissions.BasePermission):
    """
    Allows access to Managers and Admins.
    """
    def has_permission(self, request, view):
        return (
            request.user.is_authenticated and 
            request.user.role in ['MANAGER', 'ADMIN']
        )

class IsDriver(permissions.BasePermission):
    """
    Allows access to Drivers and Admins/Managers.
    """
    def has_permission(self, request, view):
        return (
            request.user.is_authenticated and 
            request.user.role in ['DRIVER', 'MANAGER', 'ADMIN']
        )

    def has_object_permission(self, request, view, obj):
        if request.user.role in ['ADMIN', 'MANAGER']:
            return True
        return getattr(obj, 'driver', None) == request.user

class IsMechanic(permissions.BasePermission):
    """
    Allows access to Mechanics and Admins/Managers.
    """
    def has_permission(self, request, view):
        return (
            request.user.is_authenticated and 
            request.user.role in ['MECHANIC', 'MANAGER', 'ADMIN']
        )

class IsGuardian(permissions.BasePermission):
    """
    Allows access to Guardians and Admins/Managers.
    """
    def has_permission(self, request, view):
        return (
            request.user.is_authenticated and 
            request.user.role in ['GUARDIAN', 'MANAGER', 'ADMIN']
        )

class IsFamilyGuardian(permissions.BasePermission):
    """
    Object-level permission to ensure a Guardian can only access their own family data.
    """
    def has_object_permission(self, request, view, obj):
        if request.user.role in ['ADMIN', 'MANAGER']:
            return True
        
        family = obj if hasattr(obj, 'primary_guardian') else getattr(obj, 'family', None)
        
        if not family:
            return False
            
        return (
            family.primary_guardian == request.user or 
            family.secondary_guardian == request.user
        )
