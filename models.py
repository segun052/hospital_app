from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager

from appt.helpers.base_model import BaseModel

USER_TYPE_CHOICES = [
    ('doc', 'Doctor'),
    ('pt', 'Patient'),
]


class UserManager(BaseUserManager):
    def create_user(self, first_name, last_name, email, username, password, type):
        user = self.model(
            first_name=first_name.capitalize(),
            last_name=last_name.capitalize(),
            email=self.normalize_email(email),
            username=username.lower(),
            type=type,
        )
        user.set_password(password)
        user.save()
        return user

    def create_staffuser(self, first_name, last_name, email, username, password):
        user = self.create_user(
            first_name=first_name,
            last_name=last_name,
            email=email,
            username=username,
            password=password,
            type='pt'
        )
        user.is_staff = True
        user.save()
        return user

    def create_superuser(self, first_name, last_name, email, username, password):
        user = self.create_user(
            first_name=first_name,
            last_name=last_name,
            email=email,
            username=username,
            password=password,
            type='pt'
        )
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user


class User(BaseModel, AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=250, verbose_name="first name")
    last_name = models.CharField(max_length=250, verbose_name="last name")
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=50, unique=True)
    telephone = models.CharField(max_length=50, blank=True, null=True)
    type = models.CharField(max_length=5, choices=USER_TYPE_CHOICES, default='pt')
    is_staff = models.BooleanField(
        "staff status",
        default=False,
        help_text="Designates whether the user can log into this admin site.",
    )

    objects = UserManager()

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["first_name", "last_name", "email"]

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        db_table = "user"
        verbose_name = "user"
        verbose_name_plural = "users"
