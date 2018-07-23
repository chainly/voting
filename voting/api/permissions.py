from rest_framework import permissions

class OwnerOnly(permissions.BasePermission):
    """Custom permission to only allow owners of an object to edit it."""

    def has_object_permission(self, request, view, obj):
        # always allow OPTIONS requests.
        if request.method in 'OPTIONS':
            return True

        # Write permissions are only allowed to the owner of the snippet.
        if hasattr(obj, 'username'):
            return obj.username == request.user
        
        return obj.owner == request.user
