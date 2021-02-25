from django.db import models
status_choices = [('new', 'Новая'), ('in_progress', 'В процессе'),  ('done', 'Сделано')]
# Create your models here.

class Task(models.Model):
    title = models.TextField(max_length=1000, null=False, blank=False, verbose_name='Задача')
    status = models.CharField(max_length=200, null=False, blank=False,choices=status_choices, default='new', verbose_name='Статус')
    time = models.DateField(null=True, blank=True)

    class Meta:
        db_table = 'Task'
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'

    def __str__(self):

        return f'{self.title} {self.status} {self.time}'