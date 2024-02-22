import logging
from django.http import HttpResponse

# логгер для записи данных о посещении страниц
logger = logging.getLogger(__name__)


def index(request):
    # "Главная" страница
    html_content = """
    <h1>Добро пожаловать на сайт Django сайт!</h1>
    <p>Это главная страница сайта.</p>
    """
    # Запись в лог о посещении страницы "Главная"
    logger.info('Страница "Главная" была посещена')
    return HttpResponse(html_content)


def about(request):
    # Страница "О себе"
    html_content = """
    <h1>О себе</h1>
    <p>Меня зовут Андрей Геннадьевич, я создатель этого сайта.</p>
    """
    # Запись в лог о посещении страницы "О себе"
    logger.info('Страница "О себе" была посещена')
    return HttpResponse(html_content)
