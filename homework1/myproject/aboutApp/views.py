from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import logging

# Инициализация логгера с именем модуля
logger = logging.getLogger(__name__)

def index(request):
    # контент страницы "Главная"
    html_content = """
    <h1>Добро пожаловать на Django сайт!</h1>
    <p>Это главная страница сайта.</p>
    """
    
   # Запись информации о посещении страницы в лог
    logger.info('Страницу "Главная" посетили')

    return HttpResponse(html_content)

def about(request):
    # контент страницы "О себе"
    html_content = """
    <h1>Обо мне</h1>
    <p>Инженер-разработчик Кира. Разработка автоматизированного комплекса расчета трудозатрат.</p>
    """
    
    # Запись информации о посещении страницы в лог
    logger.info('Страницу "О себе" посетили')

    return HttpResponse(html_content)