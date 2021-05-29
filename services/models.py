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
    amount = models.IntegerField(default=0, blank=True)

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


class Clients(models.Model):
    first_name = models.CharField(max_length=150, verbose_name='Имя')
    last_name = models.CharField(max_length=150, verbose_name='Фамилия')
    telephone_number = models.CharField(max_length=150, verbose_name='Номер телефона клиента')
    activity = models.CharField(max_length=150, verbose_name='Род деятельности', blank=True)
    birthday = models.DateField(verbose_name='День рождения', blank=True, default='10.12.2000')
    number_of_visits = models.IntegerField(default=0)
    #photo = models.ImageField(upload_to='photo/%Y/%m/%d', blank=True, verbose_name='Фото')

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'
        ordering = []

    def __str__(self):
        return str(self.first_name + ' ' + self.last_name)


class Visits(models.Model):
    client = models.ForeignKey(Clients, on_delete=models.PROTECT, verbose_name='Клиент', blank=True)
    service_name = models.ForeignKey(Services, on_delete=models.PROTECT, verbose_name='Услуга', blank=True)
    work_date = models.DateTimeField(verbose_name='Дата визита', blank=True)
    price = models.IntegerField(default='250', verbose_name='Стоимость', blank=True)
    duration = models.DurationField(default='03:00:00', help_text='часы:минуты:секунды',
                                    verbose_name='Длительность процедуры', blank=True)
    content = models.TextField(blank=True, verbose_name='Описание процедуры')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')
    photo_before = models.ImageField(upload_to='photo/%Y/%m/%d', blank=True, verbose_name='Фото до')
    photo_after = models.ImageField(upload_to='photo/%Y/%m/%d', blank=True, verbose_name='Фото после')

    # def __init__(self):
    #     super().__init__(self)
    #     self.client.number_of_visits += 1
    #     self.service_name.amount += 1


    class Meta:
        verbose_name = 'Визит'
        verbose_name_plural = 'Визиты'
        ordering = []

    def __str__(self):
        return self.service_name.service_name
