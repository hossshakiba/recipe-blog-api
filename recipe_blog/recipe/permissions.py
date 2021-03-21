from rest_framework import permissions


class IsCreatorOrReadOnly(permissions.BasePermission):
    

    def has_permission(self, request, view):
        """
        Authenticated allowed to create ingredients on List page.
        """
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        """
        Creator is allowed to Update/Delete. Others can only Retrieve.
        """
        if request.method in permissions.SAFE_METHODS:
            return True
        
        return obj.author == request.user