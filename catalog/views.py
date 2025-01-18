from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from django import forms

def home(request):
    products = Product.objects.all()
    return render(request, 'home.html', {'products': products})

def contacts(request):
    success = False
    if request.method == 'POST':
        success = True
    return render(request, 'contacts.html', {'success': success})

def product_info(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'product_info.html', {'product': product})

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'image', 'category', 'price']

def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('catalog:home')  # Перенаправление на домашнюю страницу
    else:
        form = ProductForm()
    return render(request, 'add_product.html', {'form': form})

