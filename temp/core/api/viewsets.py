from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import OrderingFilter
from rest_framework.decorators import list_route
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend

from core.models import User
from core.api.serializers import UserSerializer
from core.api.permissions import UserPermissions
from core.constants import GET



class UserViewSet(ModelViewSet):
    """
    User view set.
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = [
        DjangoFilterBackend,
        OrderingFilter,
    ]
    permission_classes = [UserPermissions, ]
    filter_fields = ["username", ]
    ordering_fields = ["id", ]
    