from django.db import models


class Services(models.Model):
    service_name = models.CharField(max_length=150, verbose_name='Наименование услуги')
    content = models.TextField(blank=True, verbose_name='Описание услуги')
    price = models.IntegerField(verbose_name='Стоимость')
    duration = models.CharField(blank=True, max_length=100, verbose_name='продолжительность')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления услуги')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')
    photo = models.ImageField(upload_to='photo/%Y/%m/%d', blank=True, verbose_name='Фото')

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'
        ordering = ['-price']

    def __str__(self):
        return self.service_name


class Cleaning(models.Model):
    step_name = models.CharField(max_length=150, verbose_name='Номер этапа')
    content = models.TextField(blank=True, verbose_name='Описание процедуры')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')
    photo = models.ImageField(upload_to='photo/%Y/%m/%d', blank=True, verbose_name='Фото')

    class Meta:
        verbose_name = 'Этап очистки'
        verbose_name_plural = 'Этапы очистки'
        ordering = []

    def __str__(self):
        return self.step_name


class Nails(models.Model):
    title = models.CharField(max_length=150, verbose_name='Вид работы')
    client_name = models.CharField(max_length=150, verbose_name='Имя клиента')
    telephone_number = models.CharField(max_length=150, verbose_name='Номер клиента')

    work_date = models.DateTimeField(verbose_name='Дата визита')
    price = models.IntegerField(verbose_name='Стоимость')
    duration = models.DurationField(verbose_name='Длительность процедуры')

    content = models.TextField(blank=True, verbose_name='Описание процедуры')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')
    photo_before = models.ImageField(upload_to='photo/%Y/%m/%d', blank=True, verbose_name='Фото до')
    photo_after = models.ImageField(upload_to='photo/%Y/%m/%d', verbose_name='Фото после')

    class Meta:
        verbose_name = 'Фото работы'
        verbose_name_plural = 'Фотографии работ'
        ordering = []

    def __str__(self):
        return self.title