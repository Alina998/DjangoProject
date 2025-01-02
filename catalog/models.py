from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование', help_text='Введите наименование категории')
    description = models.CharField(max_length=500, verbose_name='Описание', help_text='Введите описание категории')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование', help_text='Введите наименование продукта')
    description = models.CharField(max_length=500, verbose_name='Описание', help_text='Введите описание продукта')
    image = models.ImageField(upload_to='catalog/photo', blank=True, null=True, verbose_name='Фото', help_text='Загрузите фото продукта')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, verbose_name='Категория', help_text='Укажите категорию продукта', null=True, blank=True, related_name="Продукты")
    price = models.FloatField(verbose_name='Цена за покупку', help_text='Укажите цену продукта')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата последнего изменения')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
