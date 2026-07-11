from rest_framework import permissions

class IsLandlord(permissions.BasePermission):
    """Permission for Landlord role"""
    def has_permission(self, request, view):
        return request.user and request.user.role == 'landlord'


class IsTenant(permissions.BasePermission):
    """Permission for Tenant role"""
    def has_permission(self, request, view):
        return request.user and request.user.role == 'tenant'


class IsMaintenanceStaff(permissions.BasePermission):
    """Permission for Maintenance Staff role"""
    def has_permission(self, request, view):
        return request.user and request.user.role == 'maintenance'


class IsAdmin(permissions.BasePermission):
    """Permission for Admin role"""
    def has_permission(self, request, view):
        return request.user and request.user.is_staff


class IsOwnerOrReadOnly(permissions.BasePermission):
    """Allow owners to edit their own objects"""
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner == request.user


class IsPropertyOwner(permissions.BasePermission):
    """Only property owner can modify"""
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.property.owner == request.user


class IsTenantOrPropertyOwner(permissions.BasePermission):
    """Tenant can view their own records, owner can view all"""
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            if request.user.role == 'tenant':
                return obj.user == request.user
            elif request.user.role == 'landlord':
                return obj.property.owner == request.user
        return False
