from django.db import models

status_choices =(
    ('active', 'Активно'),
    ('blocked', 'Заблокировано'),
)


class Entry(models.Model):
    name = models.CharField(max_length=20, verbose_name='имя автора')
    email = models.EmailField(verbose_name='почта')
    text = models.TextField(max_length=2000, verbose_name='текст записи')
    date = models.DateTimeField( auto_now_add=True, verbose_name='дата создания')
    edit = models.DateTimeField(auto_now=True, verbose_name='время редактирования')
    status = models.CharField(max_length=20, default=status_choices[0][0], verbose_name='Статус', choices=status_choices)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Записи'
        verbose_name = 'Запись'
