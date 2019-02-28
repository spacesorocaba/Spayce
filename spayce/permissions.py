from rest_framework.permissions import BasePermission


class IsAdmin(BasePermission):
    """Custom permission class to allow only Admins to edit
    them."""

    def has_object_permission(self, request, view, obj):
        """Return True if permission is granted. """
        return request.user.is_superuser

    def has_permission(self, request, view):
        """Return True if permission is granted. """
        return request.user.is_superuser
