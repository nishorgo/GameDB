from rest_framework import permissions
from .models import Audience


class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return bool(request.user and request.user.is_staff)
    
class IsReviewOwnerOrAdmin(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        audience = Audience.objects.get(user_id=request.user.id)
        return obj.user == audience or request.user.is_staff
    
class IsReadAndUpdateAndDelete(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method == 'POST':
            return False
        return True
        