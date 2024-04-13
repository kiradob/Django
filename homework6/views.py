from django.shortcuts import render
from django.db.models import Sum
from homework5.models import Product

# Функция для подсчета общего количества продуктов в базе данных с использованием агрегации
def total_in_db(request):
    total = Product.objects.aggregate(Sum('quantity')) # Выполняем агрегацию по полю 'quantity'
    context = {'title': 'Общее количество посчитано в базе данных', 'total': total, } # Подготавливаем контекст для передачи в шаблон
    return render(request, 'total_count.html', context) # Рендерим шаблон 'total_count.html' с передачей контекста


# Функция для подсчета общего количества продуктов в представлении Python
def total_in_view(request):
    products = Product.objects.all() # Получаем все продукты из базы данных
    total = sum(product.quantity for product in products) # Считаем общее количество продуктов
    context = {'title': 'Общее количество посчитано в представлении', 'total': total, } # Подготавливаем контекст для передачи в шаблон
    return render(request, 'total_count.html', context)  # Рендерим шаблон 'total_count.html' с передачей контекста


# Функция для передачи модели продукта в шаблон для подсчета общего количества
def total_in_template(request):
    context = {'title': 'Общее количество посчитано в шаблоне', 'products': Product, } # Подготавливаем контекст с передачей модели Product
    return render(request, 'total_count.html', context) # Рендерим шаблон 'total_count.html' с передачей контекста