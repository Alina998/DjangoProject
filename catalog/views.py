from .models import Product
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView
from catalog.forms import ProductForm
from django.contrib.auth.mixins import LoginRequiredMixin


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


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'add_product.html'
    success_url = '/'

    def form_valid(self, form):
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'update_product.html'
    success_url = '/'

    def form_valid(self, form):
        return super().form_valid(form)