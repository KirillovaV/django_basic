from datetime import timedelta

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.timezone import now


class ShopUser(AbstractUser):
    avatar = models.ImageField(upload_to='users_avatars', blank=True)
    age = models.PositiveIntegerField(verbose_name='Возраст')

    activation_key = models.CharField(verbose_name='ключ подтверждения',
                                      max_length=128, blank=True)
    activation_key_expires = models.DateTimeField(verbose_name='актуальность',
                                                  default=(now() + timedelta(hours=48)))

    def is_activation_key_expired(self):
        return now() > self.activation_key_expires
