from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator


class User(AbstractUser):
    """User Model"""
    email = models.EmailField(
        verbose_name="آدرس ایمیل",
        blank=True,
        null=True,
        unique=True,
    )
    phone_number = models.CharField(
        verbose_name="شماره تلفن",
        max_length=13,
        unique=True,
        blank=True,
        null=True,
        validators=[
            RegexValidator(
                regex=r"/(^(0?9)|(\+?989))\d{9}/g",
                message="لطفا یک شماره تلفن ایرانی معتبر وارد کنید",
            )
        ],
    )


    def save(self, *args, **kwargs):
        if self.email == "":
            self.email = None
        super().save(*args, **kwargs)

    def __str__(self):
        return self.username