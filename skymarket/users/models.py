from django.contrib.auth.models import AbstractBaseUser, AbstractUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import gettext_lazy as _

from users.managers import UserManager


class UserRoles:
    # TODO закончите enum-класс для пользователя
    TYPE_ADMIN = "A"
    TYPE_USER = "U"
    STATUS_ROLE = ((TYPE_ADMIN, "admin"), (TYPE_USER, "user"))

    user_role = models.SlugField(max_length=20, unique=True, default=TYPE_USER, blank=False, null=False, choices=STATUS_ROLE)

    def __str__(self):
        return self.user_role


class User(AbstractBaseUser, PermissionsMixin):
    username = None
    email = models.EmailField(_('email_address'), unique=True, max_length=200)
    date_joined = models.DateTimeField(default=timezone.now)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    role = models.ForeignKey('UserRoles', on_delete=models.PROTECT)
    phone = PhoneNumberField()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone', "role"]

    objects = UserManager()

    @property
    def has_perm(self, perm, obj=None):
        """Does the user have a specific permission?"""
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        """Is the user a member of staff?"""
        return self.staff

    @property
    def is_admin(self):
        """Is the user a admin member?"""
        return self.admin

    def __str__(self):
        return self.email
