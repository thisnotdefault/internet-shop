from django.shortcuts import get_object_or_404, render
from django.utils import timezone

from .models import Product, ProductCategory

MENU_LINKS = [
    {"url": "main", "active": ["main"], "name": "домой"},
    {"url": "products:all", "active": ["products:all", "products:category"], "name": "продукты"},
    {"url": "contact", "active": ["contact"], "name": "контакты"},
]


def index(reqest):
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
    products = Product.objects.all()[:4]
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
    catigories = ProductCategory.objects.all()
    category = get_object_or_404(ProductCategory, pk=pk)
    products = Product.objects.filter(category=category)
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


def contact(reqest):
    return render(
        reqest,
        "mainapp/contact.html",
        context={
            "title": "Контакты",
            "menu_links": MENU_LINKS,
        },
    )
