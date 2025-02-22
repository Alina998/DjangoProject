from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.conf import settings


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование', help_text='Введите наименование категории')
    description = models.CharField(max_length=500, verbose_name='Описание', help_text='Введите описание категории')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


FORBIDDEN_WORDS = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']


def validate_forbidden_words(value):
    for word in FORBIDDEN_WORDS:
        if word.lower() in value.lower():
            raise ValidationError(f'Слово "{word}" запрещено.')

def validate_price(value):
    if value < 0:
        raise ValidationError(f'Цена не должна быть отрицательной: {value}')

def validate_image(image):
    if image:
        valid_formats = ['image/jpeg', 'image/png']
        if image.content_type not in valid_formats:
            raise ValidationError('Формат изображения должен быть JPEG или PNG.')

        max_size = 5 * 1024 * 1024  # 5 MB
        if image.size > max_size:
            raise ValidationError('Размер изображения не должен превышать 5 МБ.')


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование', help_text='Введите наименование продукта')
    description = models.CharField(max_length=500, verbose_name='Описание', help_text='Введите описание продукта')
    image = models.ImageField(upload_to='catalog/photo', blank=True, null=True, verbose_name='Фото', help_text='Загрузите фото продукта')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, verbose_name='Категория', help_text='Укажите категорию продукта', null=True, blank=True, related_name="Продукты")
    price = models.FloatField(verbose_name='Цена за покупку', help_text='Укажите цену продукта')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата последнего изменения')
    is_published = models.BooleanField(default=False)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='products', null=False, default=1)

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        permissions = [("can_unpublish_product", "Can unpublish product"), ("can_delete_product", "Can delete product"),]

    def __str__(self):
        return self.name
