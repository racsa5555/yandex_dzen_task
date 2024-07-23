from rest_framework import permissions

class IsAuthor(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.author == request.user 

class IsStaff(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user.is_staff
    
class IsAuthorOrStaff(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if obj.author == request.user:
            return True
        return request.user.is_staff