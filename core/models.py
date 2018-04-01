from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import UserManager
from django.utils.translation import ugettext_lazy as _

class User(AbstractUser):
    """
    User model.
    """

    objects = UserManager()

    class Meta:

        app_label = "core"
        verbose_name = _("user")
        verbose_name_plural = _("users")

    def __str__(self):

    	return self.username
    	