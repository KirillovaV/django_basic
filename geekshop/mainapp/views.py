from django.shortcuts import render
from mainapp.models import Product, ProductCategory


def main(request):
    title = 'Главная'
    products = Product.objects.all()
    content = {'title': title, 'products': products}
    return render(request, 'mainapp/index.html', content)


def products(request, pk=None):
    print(pk)
    title = 'каталог'
    categories = ProductCategory.objects.all()
    content = {'title': title, 'categories': categories}
    return render(request, 'mainapp/products.html', content)


def contact(request):
    return render(request, 'mainapp/contact.html', {'title': 'контакты'})
