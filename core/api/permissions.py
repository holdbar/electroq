from rest_framework.permissions import (
    BasePermission,
    SAFE_METHODS,
)
from rest_framework.permissions import IsAuthenticated

from core.constants import (
    POST,
    DELETE,
    PATCH,
)


class UserPermissions(BasePermission):
    """
    User permissions.
    """

    def has_permission(self, request, view):
        """
        List/create objects permission.

        :param request: django request instance.
        :type request: django.http.request.HttpRequest.
        :param view: view set.
        :type view: core.api.viewsets.UserViewset.
        :return: permission is granted.
        :rtype: bool.
        """

        if request.method in SAFE_METHODS:
            # Read permissions are allowed to any request, so we'll always allow GET, HEAD or OPTIONS requests.
            return True

        if request.method == POST:
            # Allow create users.
            return True

        if request.method == PATCH:
            # In futures steps of flow allow user edit self.
            return True

    def has_object_permission(self, request, view, obj):
        """
        Show/edit/delete object permission.

        :param request: django request instance.
        :type request: django.http.request.HttpRequest.
        :param view: view set.
        :type view: core.api.viewsets.UserViewset.
        :param obj: user model instance.
        :type obj: core.models.User.
        :return: permission is granted.
        :rtype: bool.
        """

        if obj == request.user:
            # Allow only owner edit objects.
            return True

        if request.method == DELETE:
            # Disallow delete users by anyone.
            return False

        if request.method in SAFE_METHODS:
            # Read permissions are allowed to any request, so we'll always allow GET, HEAD or OPTIONS requests.
            return True
