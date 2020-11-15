from rest_framework.permissions import BasePermission


class IsAdminOrReadOnlyForAuthenticated(BasePermission):

    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True
        elif request.method == "GET" and request.user.is_authenticated:
            return True
        return False