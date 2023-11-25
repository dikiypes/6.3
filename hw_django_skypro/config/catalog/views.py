from django.shortcuts import render
from django.http import HttpResponse

import json
import os


def home(request):
    # Построение пути к файлу products.json относительно базовой директории проекта
    # file_path = os.path.join(settings.BASE_DIR, 'catalog/data/products.json')

    # Чтение информации о продуктах из JSON-файла
    with open('catalog/data/products.json') as json_file:
        products_data = json.load(json_file)

    context = {
        'products': products_data,
    }

    return render(request, 'catalog/home.html', context)


def contact_view(request):
    return render(request, "catalog/contact.html")


def product_detail(request, product_id):
    with open('catalog/data/products.json') as json_file:
        products_data = json.load(json_file)
        for product_data in products_data:
            if product_data['id'] == product_id:
                break
    context = {
        'product': product_data,
    }
    return render(request, 'catalog/product_detail.html', context)
