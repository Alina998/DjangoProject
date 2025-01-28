from .models import Product
from django import forms
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView


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

class AddProductView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'add_product.html'
    success_url = '/'

    def form_valid(self, form):
        return super().form_valid(form)

