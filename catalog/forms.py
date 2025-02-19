from django import forms
from django.forms import ModelForm
from catalog.models import Product
from django.core.exceptions import ValidationError


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'image', 'category', 'price', 'is_published']

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)

        self.fields['name'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите наименование продукта'
        })

        self.fields['description'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите описание продукта'
        })

        self.fields['image'].widget.attrs.update({
            'class': 'form-control-file',
            'placeholder': 'Загрузите фото'
        })

        self.fields['category'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Укажите категорию продукта'
        })

        self.fields['price'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Укажите цену продукта'
        })

        self.fields['is_published'].widget.attrs.update({
            'class': 'form-check-input',
            'placeholder': 'Укажите статус продукта'
        })

    def clean_name(self):
        name = self.cleaned_data.get('name')
        self.validate_forbidden_words(name)
        return name

    def clean_description(self):
        description = self.cleaned_data.get('description')
        self.validate_forbidden_words(description)
        return description

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price < 0:
            raise forms.ValidationError('Цена не должна быть отрицательной.')
        return price

    def validate_forbidden_words(self, value):
        FORBIDDEN_WORDS = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']
        for word in FORBIDDEN_WORDS:
            if word.lower() in value.lower():
                raise forms.ValidationError(f'Слово "{word}" запрещено.')
