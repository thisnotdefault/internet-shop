import json

from django.shortcuts import render
from django.utils import timezone

MENU_LINKS = [
    {"url": "main", "name": "домой"},
    {"url": "products", "name": "продукты"},
    {"url": "contact", "name": "контакты"},
]


def main(reqest):
    return render(
        reqest,
        "mainapp/index.html",
        context={
            "current_year": timezone.now().year,
            "title": "Главная",
            "menu_links": MENU_LINKS,
        },
    )


def products(reqest):

    # Вариант с импортом данных из файла
    with open("./products.json", "r") as file:
        products = json.load(file)

    # Вариант простого списка
    # products = [
    #     {
    #         'name': 'Люстра',
    #         'description': 'Цветная люстра',
    #         'image': 'img/product-11.jpg'
    #     },
    #     {
    #         'name': 'Cтул',
    #         'description': 'Удобный стул',
    #         'image': 'img/product-21.jpg'
    #     },
    #     {
    #         'name': 'Лампа',
    #         'description': 'Уютная лампа',
    #         'image': 'img/product-31.jpg'
    #     },
    # ]

    return render(
        reqest,
        "mainapp/products.html",
        context={
            "title": "Продукты",
            "menu_links": MENU_LINKS,
            "products": products,
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
