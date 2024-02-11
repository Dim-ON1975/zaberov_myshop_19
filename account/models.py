from django.db import models
from django.contrib.auth.models import AbstractUser
from catalog.models import NULLABLE


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='электронная почта')

    phone = models.CharField(max_length=35, **NULLABLE, verbose_name='телефон')
    avatar = models.ImageField(upload_to='users/%Y/%m/%d/', **NULLABLE, verbose_name='аватар')
    country = models.CharField(max_length=100, verbose_name='страна', **NULLABLE)

    email_verify = models.BooleanField(default=False, verbose_name='верификация почты')

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
