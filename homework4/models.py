from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    added_date = models.DateField(auto_now_add=True)
    image = models.ImageField(upload_to='product_images/', null=True, blank=True)  # для хранения фото продукта

    def __str__(self):
        return self.name