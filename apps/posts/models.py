from django.db import models

# Create your models here.


class Post(models.Model):
    title = models.CharField( # оюязательно это max 
        max_length=100, verbose_name='Название'
    )
    description = models.CharField(
        max_length=1000, verbose_name='Описание',
        blank=True # если не добавть ничего не будет
    )
    price = models.IntegerField( # нет обяз. но принято писать default 
        default=0, verbose_name='Цена'
    )
    ingredients = models.CharField(
        max_length=1000, verbose_name='Ингридиенты'
    )
    image = models.ImageField( # обяз поле upload_to
        upload_to='flowers_img', null=True # можеть быть null
    )
