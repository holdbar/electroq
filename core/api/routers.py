from rest_framework.routers import DefaultRouter

from core.api.viewsets import UserViewSet

router = DefaultRouter()

# registering viewsets
router.register(r"user", UserViewSet)
