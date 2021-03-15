from rest_framework import permissions


class IsAdminOrReadOnly(permissions.BasePermission):
    
    message = 'Only Admin/Staff are allowed.'

    def has_permission(self, request, view):
        """
        Admin/Staff are allowed to Write. Others can only Read.
        """
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_staff

    def has_object_permission(self, request, view, obj):
        """
        Admin/Staff are allowed to Update/Delete. Others can only Retrieve.
        """
        if request.method in permissions.SAFE_METHODS:
            return True
        
        return request.user.is_staff