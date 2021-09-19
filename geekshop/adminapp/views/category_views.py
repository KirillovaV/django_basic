from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import HttpResponseRedirect, get_object_or_404
from django.shortcuts import render
from django.urls import reverse
from mainapp.models import ProductCategory
from mainapp.forms import ProductCategoryEditForm


@user_passes_test(lambda u: u.is_superuser)
def categories(request):
    title = 'Админка/категории'

    category_list = ProductCategory.objects.all().order_by('name')
    content = {
        'title': title,
        'objects': category_list,
    }
    return render(request, 'adminapp/categories.html', content)


@user_passes_test(lambda u: u.is_superuser)
def category_create(request):
    title = 'категории/создание'

    if request.method == 'POST':
        category_form = ProductCategoryEditForm(request.POST, request.FILES)
        if category_form.is_valid():
            category_form.save()
            return HttpResponseRedirect(reverse('admin:categories'))
    else:
        category_form = ProductCategoryEditForm()

    content = {
        'title': title,
        'update_form': category_form
    }
    return render(request, 'adminapp/category_update.html', content)


@user_passes_test(lambda u: u.is_superuser)
def category_update(request, pk):
    title = 'категории/редактирование'
    edit_category = get_object_or_404(ProductCategory, pk=pk)

    if request.method == 'POST':
        category_form = ProductCategoryEditForm(request.POST, request.FILES, instance=edit_category)
        if category_form.is_valid():
            category_form.save()
            return HttpResponseRedirect(reverse('admin:category_update', args=[edit_category.pk]))
    else:
        category_form = ProductCategoryEditForm(instance=edit_category)

    content = {
        'title': title,
        'update_form': category_form
    }
    return render(request, 'adminapp/category_update.html', content)


@user_passes_test(lambda u: u.is_superuser)
def category_delete(request, pk):
    title = 'категории/удаление'
    category = get_object_or_404(ProductCategory, pk=pk)

    if request.method == 'POST':
        category.is_active = False
        category.save()
        return HttpResponseRedirect(reverse('admin:categories'))

    content = {
        'title': title,
        'category_to_delete': category
    }
    return render(request, 'adminapp/category_delete.html', content)
