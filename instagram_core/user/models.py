from django.contrib.auth.models import AbstractBaseUser
from django.db import models

from user.manager import CustomUserManager


class CustomUser(AbstractBaseUser):
    DoesNotExist = None
    username = models.CharField(max_length=255, unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self):
        return self.username
