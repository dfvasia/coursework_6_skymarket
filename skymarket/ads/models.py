from django.conf import settings
from django.db import models
from django.utils import timezone

from users.models import User


class Ad(models.Model):
    title = models.CharField(max_length=128, blank=False, null=False, verbose_name='Текст сообщения')
    price = models.PositiveSmallIntegerField(null=False, blank=False, verbose_name='Стоимость')
    description = models.CharField(max_length=128, blank=False, null=False, verbose_name='Текст объявления')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='ИД пользователя')
    created_at = models.DateTimeField(default=timezone.now, verbose_name='Дата создания')
    image = models.ImageField(upload_to='images/', null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Объявление"
        verbose_name_plural = "Объявления"
        ordering = ['pk']



class Comment(models.Model):
    text = models.CharField(max_length=128, blank=False, null=False, verbose_name='Текст сообщения')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='ИД пользователя комментария')
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE, verbose_name='ИД сообщения')
    created_at = models.DateTimeField(default=timezone.now, verbose_name='Дата создания')
