from django.db import models


class Products(models.Model):
        title = models.CharField('Наименование', max_length=50)
        price = models.IntegerField('Цена')
        image = models.TextField('Ссылка на картинку')


class Comments(models.Model):
        name = models.CharField('Имя', max_length=50)
        comment = models.TextField('Отзыв')


class Locations(models.Model):
        title = models.CharField('Наименование', max_length=50)
        location = models.TextField('Адрес')


class Promos(models.Model):
        title = models.CharField('Наименование', max_length=50)
        desription = models.TextField('Описание')


class Sales(models.Model):
        title = models.CharField('Наименование', max_length=50)
        price = models.IntegerField('Цена')
        image = models.TextField('Ссылка на картинку')


class Makers(models.Model):
        title = models.CharField('Наименование', max_length=50)
        product = models.CharField('Наименование', max_length=50)
        email = models.CharField('Наименование', max_length=50)


