from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _


class User(AbstractUser):
    """
    Custom user model with unique email address and special membership attribute
    """
    email = models.EmailField(_("email"), max_length=254, unique=True)
    is_special = models.DateTimeField(_("special member until"), default=timezone.now)

    REQUIRED_FIELDS = ['email', ]

    def is_special_member(self):
        """
        returns True if a user is a special member.
        spcial members have access to all the recipes.
        """
        if self.is_superuser or self.is_staff:
            return True
        return self.is_special > timezone.now()
