from django.urls import path
from .views import total_in_db, total_in_view, total_in_template

# Определяем маршруты URL для вызова соответствующих представлений
urlpatterns = [
    path('db/', total_in_db, name='db'), # URL-адрес для подсчета общего количества через базу данных
    path('view/', total_in_view, name='view'), # URL-адрес для подсчета общего количества 
    path('template/', total_in_template, name='template'), # URL-адрес для подсчета общего количества через передачу модели в шаблон
]