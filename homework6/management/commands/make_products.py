from random import choice, randint, uniform
from django.core.management.base import BaseCommand
from homework5.models import Category, Product

class Command(BaseCommand):
    help = "Generate fake products."

# Добавляем аргумент командной строки 'count', который будет указывать количество создаваемых продуктов
    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='User ID')

 # Метод handle будет вызываться при выполнении команды для генерации фейковых продуктов
    def handle(self, *args, **kwargs):
        categories = Category.objects.all() # Получаем все категории продуктов из базы данных
        products = []  # Создаем список для хранения сгенерированных продуктов
        count = kwargs.get('count')  # Получаем количество продуктов из аргумента командной строки


# Генерируем указанное количество продуктов
        for i in range(1, count + 1):
            products.append(Product(name=f'продукт номер {i}', # Генерируем имя продукта
                                    category=choice(categories), # Выбираем случайную категорию из списка
                                    description='длинное описание продукта, которое и так никто не читает', # Задаем описание продукта
                                    price=uniform(0.01, 999_999.99), # Генерируем случайную цену 
                                    quantity=randint(1, 10_000), # Генерируем случайное количество
                                    rating=uniform(0.01, 9.99), ))  # Генерируем случайный рейтинг
        Product.objects.bulk_create(products) # Массово добавляем созданные продукты в базу данных