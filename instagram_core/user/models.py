from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=128)
    class Meta:
        verbose_name_plural = 'Пользователи'
        verbose_name = 'Пользователь'
