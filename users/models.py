from django.db import models


class User(models.Model):
    username = models.CharField('user name', max_length=400, unique=True)
    email = models.EmailField('email', unique=True)
    password = models.CharField('password', max_length=400)
    objects = models.Manager()

    class Meta:
        verbose_name = 'user data'
        verbose_name_plural = 'user data'

    def __str__(self):
        return f'{self.username} & {self.email}'
