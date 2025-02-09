from django.forms import ModelForm
from catalog.models import Product


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'image', 'category', 'price']

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)

        # Настройка атрибутов виджета для поля 'name'
        self.fields['name'].widget.attrs.update({
            'class': 'form-control',  # Добавление CSS-класса для стилизации поля
            'placeholder': 'Введите наименование продукта'  # Текст подсказки внутри поля
        })

        # Настройка атрибутов виджета для поля 'description'
        self.fields['description'].widget.attrs.update({
            'class': 'form-control',  # Добавление CSS-класса для стилизации поля
            'placeholder': 'Введите описание продукта'  # Текст подсказки внутри поля
        })

        # Настройка атрибутов виджета для поля 'image'
        self.fields['image'].widget.attrs.update({
            'class': 'form-control-file',  # Добавление CSS-класса для стилизации поля
            'placeholder': 'Загрузите фото'  # Текст подсказки внутри поля
        })

        # Настройка атрибутов виджета для поля 'category'
        self.fields['category'].widget.attrs.update({
            'class': 'form-control',  # Добавление CSS-класса для стилизации поля
            'placeholder': 'Укажите категорию продукта'  # Текст подсказки внутри поля
        })

        # Настройка атрибутов виджета для поля 'price'
        self.fields['price'].widget.attrs.update({
            'class': 'form-control',  # Добавление CSS-класса для стилизации поля
            'placeholder': 'Укажите цену продукта'  # Текст подсказки внутри поля
        })
