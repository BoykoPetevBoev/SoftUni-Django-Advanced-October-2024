from django.db import models
from django.contrib.auth.models import AbstractUser,  PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django_advanced.user_app.managers import CustomUserManager

class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        unique=True,
    )

    is_active = models.BooleanField(
        default=True,
    )

    is_staff = models.BooleanField(
        default=False,
    )

    USERNAME_FIELD = "email"

    objects = CustomUserManager()