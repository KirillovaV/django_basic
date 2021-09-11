from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from basketapp.models import Basket
from mainapp.models import Product


def basket(request):
    title = 'корзина'
    basket = request.user.basket.all()
    content = {'title': title, 'basket': basket}
    return render(request, 'basketapp/basket.html', content)


def basket_add(request, pk):
    product = get_object_or_404(Product, pk=pk)
    basket = Basket.objects.filter(user=request.user, pk=pk).first()

    if not basket:
        basket = Basket(user=request.user, product=product)

    basket.quantity += 1
    basket.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def basket_remove(request, pk):
    basket = Basket.objects.filter(user=request.user, pk=pk)
    basket[0].quantity -= 1
    basket[0].save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))