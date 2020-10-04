from rest_framework import permissions

class IsAuthorOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        
        # Here read permission are allowed for any request
        # But later change to logged in one in views.py
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only required to author of post
        return obj.author == request.user