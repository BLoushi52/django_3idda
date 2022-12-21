from rest_framework.permissions import BasePermission

class IsCreator(BasePermission):
    message = "You must be the creator of this item."

    def has_object_permission(self, request, view, obj):
        return  obj.user == request.user
