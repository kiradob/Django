from django.contrib import admin
from .models import Category, Product, Client, Order, OrderProduct

# Определение действия администратора для сброса количества продуктов в ноль
@admin.action(description="Сбросить количество в ноль")
def reset_quantity(modeladmin, request, queryset):
    queryset.update(quantity=0)

# Настройка администрирования модели продукта
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'price', 'quantity'] # Отображаемые поля в списке продуктов
    ordering = ['category', '-quantity'] # Порядок сортировки
    list_filter = ['date_added', 'price'] # Фильтры для списка продуктов
    search_fields = ['description'] # Поля для поиска
    search_help_text = 'Поиск по полю Описание продукта (description)' # Подсказка для поиска
    actions = [reset_quantity] # Действие для сброса количества продуктов в ноль

    readonly_fields = ['date_added', 'rating'] # Поля только для чтения
    # Настройка полей для редактирования
    fieldsets = [(None, {'classes': ['wide'], 'fields': ['name'], }, ), ('Подробности', {'classes': ['collapse'], 'description': 'Категория товара и его подробное описание', 'fields': ['category', 'description'], },),
                 ('Бухгалтерия', {'fields': ['price', 'quantity'], }), ('Рейтинг и прочее', {'description': 'Рейтинг сформирован автоматически на основе оценок покупателей', 'fields': ['rating', 'date_added'], }),]

# Настройка администрирования модели клиента
class ClientAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone_number', 'address', 'registration_date'] # Отображаемые поля в списке клиентов
    list_filter = ['registration_date'] # Фильтры для списка клиентов
    search_fields = ['name', 'email'] # Поля для поиска
    ordering = ['registration_date'] # Порядок сортировки
    readonly_fields = ['registration_date'] # Поля только для чтения
# Определение класса Inline для отображения продуктов в заказе на странице заказа в административной панели
class OrderProductInline(admin.TabularInline):
    model = OrderProduct
    extra = 1
# Настройка администрирования модели заказа
class OrderAdmin(admin.ModelAdmin):
    list_display = ['client', 'total_amount', 'order_date'] # Отображаемые поля в списке заказов
    list_filter = ['order_date'] # Фильтры для списка заказов
    search_fields = ['client__name'] # Поля для поиска
    ordering = ['-order_date'] # Порядок сортировки
    readonly_fields = ['order_date'] # Поля только для чтения
    inlines = [OrderProductInline] # Встраивание информации о продуктах в заказ на странице заказа

# Регистрация моделей в административной панели Django с соответствующими настройками
admin.site.register(Client, ClientAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Category)
admin.site.register(Product, ProductAdmin)