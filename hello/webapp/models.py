from django.db import models

# Create your models here.

class Article(models.Model):
    title = models.TextField(max_length=1000, null=False, blank=False, verbose_name='Задача')
    status = models.CharField(max_length=200, null=False, blank=False, default='Unknown', verbose_name='Статус')
    time = models.CharField(max_length=200, null=True, blank=True, default='New')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Время изменения')

    class Meta:
        db_table = 'articles'
        verbose_name = 'Задача'
        verbose_name_plural = 'Статус'

    def __str__(self):

        return f'{self.title} {self.status} {self.time}'