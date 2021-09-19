from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import get_object_or_404, render
from mainapp.models import ProductCategory, Product


@user_passes_test(lambda u: u.is_superuser)
def products(request, pk):
    title = 'Админка/продукт'

    category = get_object_or_404(ProductCategory, pk=pk)
    product_list = Product.objects.filter(category__pk=pk).order_by('name')
    content = {
        'title': title,
        'category': category,
        'objects': product_list,
    }
    return render(request, 'adminapp/products.html', content)


@user_passes_test(lambda u: u.is_superuser)
def product_create(request, pk):
    pass


@user_passes_test(lambda u: u.is_superuser)
def product_update(request, pk):
    pass


@user_passes_test(lambda u: u.is_superuser)
def product_read(request, pk):
    pass


@user_passes_test(lambda u: u.is_superuser)
def product_delete(request, pk):
    pass
