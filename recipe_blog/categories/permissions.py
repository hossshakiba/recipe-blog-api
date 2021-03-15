from rest_framework import permissions


class IsAdminOrReadOnly(permissions.BasePermission):
    """
    Object-level permission to only allow staffs to update/delete.
    """
    message = 'Only Admin/Staff are allowed.'

    def has_permission(self, request, view):
        """
        Return `True` if permission is granted, `False` otherwise.
        """
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_staff

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        

