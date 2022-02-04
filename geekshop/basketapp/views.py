from django.http.response import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render

from mainapp.models import Product

from .models import Basket


def view(request):
    return render(request, 'basketapp/basket.html', context={
        'basket': Basket.objects.filter(user=request.user)
    })


def add(request, product_id):
    product = get_object_or_404(Product,pk=product_id)
    basket_items = Basket.objects.filter(user=request.user, product=product)

    if basket_items:
        basket = basket_items[0]
    else:
        basket = Basket(user=request.user, product=product)

    basket.quantity += 1
    basket.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def remove(request,basket_item_id):
    basket = get_object_or_404(Basket, pk=basket_item_id)
    basket.delete()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
