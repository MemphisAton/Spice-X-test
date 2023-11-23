from django.db import models


class Advantage(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=100, blank=True)
    content = models.TextField(blank=True)
    link = models.URLField(blank=True)

    class Meta:
        verbose_name = 'Преимущество'
        verbose_name_plural = 'Преимущества'

    def __str__(self):
        return self.title


class MenuItem(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название')
    link = models.URLField(blank=True)

    class Meta:
        verbose_name = 'Пункт меню'
        verbose_name_plural = 'Пункты меню'

    def __str__(self):
        return self.name
