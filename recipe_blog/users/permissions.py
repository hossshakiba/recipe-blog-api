from rest_framework import permissions

class IsCreator(permissions.BasePermission):
    """
    Object-level permission to only allow creators of an object to edit/delete it.
    """
    message = 'You must be the creator of this object.'

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return request.user and request.user.is_authenticated
        return obj == request.user
