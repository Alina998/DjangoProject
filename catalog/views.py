from .models import Product
from django import forms
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView
from django.core.exceptions import ValidationError


class HomeView(ListView):
    model = Product
    template_name = 'home.html'
    context_object_name = 'products'

class ContactsView(TemplateView):
    template_name = 'contacts.html'

    def post(self, request, *args, **kwargs):
        return self.render_to_response({'success': True})

class ProductInfoView(DetailView):
    model = Product
    template_name = 'product_info.html'
    context_object_name = 'product'

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'image', 'category', 'price']

    def validate_forbidden_words(self, value):
        FORBIDDEN_WORDS = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']
        for word in FORBIDDEN_WORDS:
            if word.lower() in value.lower():
                raise forms.ValidationError(f'Слово "{word}" запрещено.')

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

    def validate_image(image):
        if image:
            valid_formats = ['image/jpeg', 'image/png']
            if image.content_type not in valid_formats:
                raise ValidationError('Формат изображения должен быть JPEG или PNG.')

            max_size = 5 * 1024 * 1024  # 5 MB
            if image.size > max_size:
                raise ValidationError('Размер изображения не должен превышать 5 МБ.')
            return image

class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'add_product.html'
    success_url = '/'

    def form_valid(self, form):
        return super().form_valid(form)


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'update_product.html'
    success_url = '/'

    def form_valid(self, form):
        return super().form_valid(form)