from django.shortcuts import render, redirect
from .models import Product
from django import forms


# def home(request):
#     latest_products = Product.objects.order_by('-created_at')[:5]
#     return render(request, 'home.html', {'latest_products': latest_products})


from django.core.paginator import Paginator

def home(request):
    products = Product.objects.all()
    return render(request, 'home.html', {'products': products})


def contacts(request):
    success = False
    if request.method == 'POST':
        success = True
    return render(request, 'contacts.html', {'success': success})


def product_info(request):
    products = Product.objects.all()
    return render(request, 'product_info.html', {'products' : products})


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'image', 'category', 'price']

def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')  # Перенаправление на домашнюю страницу
    else:
        form = ProductForm()
    return render(request, 'add_product.html', {'form': form})
