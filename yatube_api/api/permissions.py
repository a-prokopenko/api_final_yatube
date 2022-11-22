from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
    """
    Кастомное ограничение, позволяющее только авторам редактировать пост.
    """

    message = 'У вас недостаточно прав для выполнения данного действия.'

    def has_permission(self, request, view):
        return bool(
            request.method in permissions.SAFE_METHODS or request.user
            and request.user.is_authenticated
        )

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user
