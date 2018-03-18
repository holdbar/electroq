from django.conf.urls import url, include
from core import views as core_views


from rest_framework.authtoken import views


urlpatterns = [
    url(r'^api-token-auth/', views.obtain_auth_token),
]

