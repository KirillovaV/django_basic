from django.shortcuts import render


def main(request):
    return render(request, 'mainapp/index.html', {'title': 'магазин'})


def products(request):
    return render(request, 'mainapp/products.html', {'title': 'каталог'})


def contact(request):
    return render(request, 'mainapp/contact.html', {'title': 'контакты'})
