from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class ShopUser(AbstractUser):
    age = models.PositiveIntegerField(verbose_name="возраст")
    avatar = models.ImageField(verbose_name="аватар", blank=True, upload_to="users")
    phone = models.CharField(
        max_length=20,
        verbose_name="телефон",
        blank=True,
    )
    city = models.CharField(max_length=20, verbose_name="город", blank=True)
