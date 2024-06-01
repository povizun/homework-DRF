from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {"blank": True, "null": True}


class User(AbstractUser):
    username = None

    email = models.EmailField(
        unique=True, verbose_name="почта", help_text="Введите почту"
    )

    phone = models.CharField(
        max_length=35,
        **NULLABLE,
        verbose_name="номер телефона",
        help_text="Укажите ваш номер"
    )
    city = models.CharField(
        max_length=35, **NULLABLE, verbose_name="город", help_text="Укажите ваш город"
    )
    avatar = models.ImageField(
        upload_to="users/avatars",
        **NULLABLE,
        verbose_name="Аватар",
        help_text="Загрузите ваш аватар"
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
