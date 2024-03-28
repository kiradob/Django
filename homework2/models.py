from django.db import models

class Client(models.Model):
    name = models.CharField(max_length=100) # Имя клиента
    email = models.EmailField() # Email клиента
    phone_number = models.CharField(max_length=20) # Номер телефона клиента
    address = models.TextField() # Адрес клиента
    registration_date = models.DateField(auto_now_add=True) # Дата регистрации клиента

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100) # Наименование продукта
    description = models.TextField() # Описание продукта
    price = models.DecimalField(max_digits=10, decimal_places=2) # Цена продукта
    quantity = models.IntegerField() # Количество продукта на складе
    added_date = models.DateField(auto_now_add=True) # Дата добавления продукта

    def __str__(self):
        return self.name

class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE) # Связь с клиентом, к которому относится заказ
    products = models.ManyToManyField(Product) # Продукты, входящие в заказ
    total_amount = models.DecimalField(max_digits=10, decimal_places=2) # Общая сумма заказа
    order_date = models.DateField(auto_now_add=True) # Дата оформления заказа

    def __str__(self):
        return f'Order for {self.client}'