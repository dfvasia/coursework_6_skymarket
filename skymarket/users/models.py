import enum

from django.contrib.auth.models import AbstractBaseUser, AbstractUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import gettext_lazy as _

from users.managers import UserManager


class UserRoles(enum.Enum):
    ADMIN = "admin"
    USER = "user"


class User(AbstractBaseUser, PermissionsMixin):
    username = None
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(_('email_address'), unique=True, max_length=200)
    date_joined = models.DateTimeField(default=timezone.now, verbose_name='Дата создания')
    is_active = models.BooleanField(default=False, verbose_name='Статус')
    role = models.CharField(max_length=15, blank=False, null=False, default=UserRoles.USER, verbose_name='Группа доступа')
    phone = PhoneNumberField(verbose_name='Телефон')
    user_permissions = models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='Разрешения')
    groups = models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='Группы')
    password = models.CharField(max_length=128, verbose_name='ХЕШ пароля')
    last_login = models.DateTimeField(blank=True, null=True, verbose_name='Последний вход')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone']

    objects = UserManager()

    @property
    def is_admin(self):
        return self.role == UserRoles.ADMIN

    @property
    def is_user(self):
        return self.role == UserRoles.USER

    @property
    def is_superuser(self):
        return self.is_admin

    @property
    def is_staff(self):
        return self.is_admin

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return self.is_admin

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'пользователи'
