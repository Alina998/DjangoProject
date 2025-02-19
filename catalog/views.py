from .models import Product
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from catalog.forms import ProductForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin


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
        form.instance.owner = self.request.user
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'update_product.html'
    success_url = reverse_lazy('catalog:home')
    permission_required = 'catalog.change_product'

    def form_valid(self, form):
        return super().form_valid(form)

    def handle_no_permission(self):
        return super().handle_no_permission()

    def test_func(self):
        product = self.get_object()
        return self.request.user == product.owner


class ProductDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Product
    template_name = 'delete_product.html'
    success_url = reverse_lazy('home')
    permission_required = 'catalog.can_delete_product'

    def handle_no_permission(self):
        return super().handle_no_permission()

    def test_func(self):
        product = self.get_object()
        return self.request.user == product.owner


class ProductUnpublishView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'unpublish_product.html'
    success_url = reverse_lazy('home')
    permission_required = 'catalog.can_unpublish_product'

    def test_func(self):
        product = self.get_object()
        return self.request.user == product.owner