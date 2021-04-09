import uuid

from django.db import models


class Queue(models.Model):
    uuid = models.UUIDField('Другорядний первинний ключ', unique=True, blank=True)

    created = models.DateTimeField('Дата створення', auto_now_add=True)

    start_date = models.DateTimeField('Час початку заняття')
    creator = models.ForeignKey('user_profile.User', on_delete=models.SET_NULL, null=True,
                                verbose_name='Автор черги')

    class Meta:
        verbose_name = 'Черга'
        verbose_name_plural = 'Черги'

    def save(self, *args, **kwargs):
        if not self.uuid:
            self.uuid = uuid.uuid4()

        super().save(*args, **kwargs)
