from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import HttpResponseRedirect, get_object_or_404, render
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import DetailView, DeleteView, ListView, CreateView, UpdateView
from mainapp.models import ProductCategory, Product
from adminapp.forms import ProductEditForm


# class ProductsView(ListView):
#     model = Product
#     template_name = 'adminapp/products.html'
#
#     @method_decorator(user_passes_test(lambda u: u.is_superuser))
#     def dispatch(self, *args, **kwargs):
#         self.queryset = Product.objects.filter(category__pk=self.kwargs['pk']).order_by('name')
#         return super().dispatch(*args, **kwargs)


@user_passes_test(lambda u: u.is_superuser)
def products(request, pk):
    title = 'Админка/продукт'

    category = get_object_or_404(ProductCategory, pk=pk)
    product_list = Product.objects.filter(category__pk=pk).order_by('name')
    content = {
        'title': title,
        'category': category,
        'object_list': product_list,
    }
    return render(request, 'adminapp/products.html', content)


# class ProductCreateView(View):
#     form_class = ProductEditForm
#     template_name = 'adminapp/product_update.html'
#
#     def get(self, request, *args, **kwargs):
#         category = get_object_or_404(ProductCategory, pk=self.kwargs['pk'])
#         form = self.form_class(initial={'category': category})
#         content = {
#             'form': form,
#             'category': category,
#             'title': 'продукт/создание',
#         }
#         return render(request, self.template_name, content)
#
#     def post(self, request, *args, **kwargs):
#         form = self.form_class(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('admin:products', args=self.kwargs['pk']))


@user_passes_test(lambda u: u.is_superuser)
def product_create(request, pk):
    title = 'продукт/создание'
    category = get_object_or_404(ProductCategory, pk=pk)

    if request.method == 'POST':
        product_form = ProductEditForm(request.POST, request.FILES)
        if product_form.is_valid():
            product_form.save()
            return HttpResponseRedirect(reverse('admin:products', args=[pk]))
    else:
        product_form = ProductEditForm(initial={'category': category})

    content = {'title': title,
               'form': product_form,
               'category': category,
               }
    return render(request, 'adminapp/product_update.html', content)


# class ProductUpdateView(UpdateView):
#     model = Product
#     template_name = 'adminapp/product_update.html'
#     fields = '__all__'


@user_passes_test(lambda u: u.is_superuser)
def product_update(request, pk):
    title = 'продукт/редактирование'
    edit_product = get_object_or_404(Product, pk=pk)

    if request.method == 'POST':
        edit_form = ProductEditForm(request.POST, request.FILES, instance=edit_product)
        if edit_form.is_valid():
            edit_form.save()
            return HttpResponseRedirect(reverse('admin:product_update', args=[edit_product.pk]))
    else:
        edit_form = ProductEditForm(instance=edit_product)

    content = {'title': title,
               'form': edit_form,
               'category': edit_product.category,
               }
    return render(request, 'adminapp/product_update.html', content)


class ProductReadView(DetailView):
    model = Product
    template_name = 'adminapp/product_read.html'


# @user_passes_test(lambda u: u.is_superuser)
# def product_read(request, pk):
#     title = 'продукт/подробнее'
#     product = get_object_or_404(Product, pk=pk)
#
#     content = {
#         'title': title,
#         'object': product,
#     }
#     return render(request, 'adminapp/product_read.html', content)


class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'adminapp/product_delete.html'

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_active = False
        self.object.save()

        return HttpResponseRedirect(reverse('admin:products', args=[self.object.category.pk]))


# @user_passes_test(lambda u: u.is_superuser)
# def product_delete(request, pk):
#     title = 'продукт/удаление'
#     product = get_object_or_404(Product, pk=pk)
#
#     if request.method == 'POST':
#         product.is_active = False
#         product.save()
#         return HttpResponseRedirect(reverse('admin:products', args=[product.category.pk]))
#
#     content = {
#         'title': title,
#         'product_to_delete': product,
#     }
#     return render(request, 'adminapp/product_delete.html', content)
