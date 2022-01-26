from django.shortcuts import render
from django.utils import timezone

from .models import Product, ProductCategory

MENU_LINKS = [
    {"url": "main", "name": "домой"},
    {"url": "mainapp:products", "name": "продукты"},
    {"url": "contact", "name": "контакты"},
]


def main(reqest):
    products = Product.objects.all()[:4]
    return render(
        reqest,
        "mainapp/index.html",
        context={
            "current_year": timezone.now().year,
            "title": "Главная",
            "menu_links": MENU_LINKS,
            "products": products,
        },
    )


def products(reqest):
    catigories = ProductCategory.objects.all()
    return render(
        reqest,
        "mainapp/products.html",
        context={
            "title": "Продукты",
            "menu_links": MENU_LINKS,
            "products": products,
            "catigories": catigories,
        },
    )


def category(reqest, pk):
    return products(reqest)


def contact(reqest):
    return render(
        reqest,
        "mainapp/contact.html",
        context={
            "title": "Контакты",
            "menu_links": MENU_LINKS,
        },
    )
