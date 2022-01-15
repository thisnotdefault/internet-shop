from django.shortcuts import render

def main(reqest):
    return render(reqest, 'mainapp/index.html')

def products(reqest):
    return render(reqest, 'mainapp/products.html')

def contact(reqest):
    return render(reqest, 'mainapp/contact.html')

