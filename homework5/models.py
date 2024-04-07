from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True) # Поле для названия категории
    def __str__(self):
        return self.name # Возвращает название категории в виде строки

class Product(models.Model):
    name = models.CharField(max_length=50) # Поле для названия продукта
    category = models.ForeignKey(Category, on_delete=models.CASCADE) # Ссылка на категорию продукта
    description = models.TextField(default='Это прекрасный продукт!', blank=True) # Описание продукта
    price = models.DecimalField(default=100.00, max_digits=8, decimal_places=2) # Цена продукта
    quantity = models.PositiveSmallIntegerField(default=0) # Количество продукта в наличии
    date_added = models.DateTimeField(auto_now_add=True) # Дата добавления продукта
    rating = models.DecimalField(default=5.0, max_digits=3, decimal_places=2) # Рейтинг продукта (по умолчанию 5)
    def __str__(self):
        return self.name # Возвращение названияе категории в виде строки

@property
def total_quantity(self):
    return sum(product.quantity for product in Product.objects.all()) # Вычисление общего количества продуктов

class Client(models.Model):
    name = models.CharField(max_length=100) # Поле для имени клиента
    email = models.EmailField() # Поле для email клиента
    phone_number = models.CharField(max_length=20) # Поле для номера телефона клиента
    address = models.TextField() # Поле для адреса клиента
    registration_date = models.DateField(auto_now_add=True) # Дата регистрации клиента
    def __str__(self):
        return self.name  # Возвращение имени клиента в виде строки

class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE) # Ссылка на клиента, сделавшего заказ
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)  # Общая сумма заказа
    order_date = models.DateField(auto_now_add=True) # Дата оформления заказа
    
    def str(self):
        return f'Order for {self.client}'  # Возвращение строки с информацией о заказе

class OrderProduct(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE) # Ссылка на заказ
    product = models.ForeignKey(Product, on_delete=models.CASCADE) # Ссылка на продукт в заказе
    quantity = models.PositiveSmallIntegerField(default=1) # Количество продукта в заказе
    def save(self, *args, **kwargs):
        self.price_per_item = self.product.price # Цена продукта в заказе
        self.total_price = self.quantity * self.price_per_item # Общая цена за продукт в заказе
        self.order.total_amount += self.total_price # Обновление общей суммы заказа
        self.order.save() # Сохранение изменений в заказе
        super(OrderProduct, self).save(*args, **kwargs) # Сохранение объекта OrderProduct