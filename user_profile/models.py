from django.db import models
from django_use_email_as_username.models import BaseUser, BaseUserManager


class User(BaseUser):
    objects = BaseUserManager()

    uni_group = models.ForeignKey('user_profile.UniGroup', on_delete=models.SET_NULL, null=True, blank=True,
                                  verbose_name='Університетська група')


class Faculty(models.Model):
    name = models.CharField('Назва', max_length=200, unique=True)

    class Meta:
        verbose_name = 'Факультет'
        verbose_name_plural = 'Факультети'

    def __str__(self):
        return self.name


class UniGroup(models.Model):
    name = models.CharField('Назва', max_length=50, unique=True)
    faculty = models.ForeignKey('user_profile.Faculty', on_delete=models.CASCADE, verbose_name='Факультет')

    class Meta:
        verbose_name = 'Університетська група'
        verbose_name_plural = 'Університетські групи'

    def __str__(self):
        return self.name
