from rest_framework import permissions
from rest_framework.response import Response

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """
    

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.user == request.user

class IsAdmin(permissions.BasePermission):
    edit_methods = ("PUT", "PATCH")
    """
    Custom permission to only allow admin to edit it status.
    """
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True
    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser:
            return True
    
        if request.user.userType == 'ADMIN':
            return True
        if request.method not in  self.edit_methods:
            return Response("Operation Not Permitted to this user")

        return False