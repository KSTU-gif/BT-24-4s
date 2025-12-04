Import sys 
from PyQt5 QtWidgets import QApplication, QPushButton, QLabel, Q

class Basebutton:
    """Базовый интерфейс для декорирования"""
    def click(self):
        print("Base button clicked")

def get_widget(self):
    """Вовращает реальный QpushButton"""
    raise NotImplementedError

class SimpleButton(Basebutton):
    """обычная кнопка"""
    def_init_(self, text):
    self.btn = QPushButton(text)

def get_widget(self):
    return self.btn

def logging_decorator(func):
    """Декоратор для логирования вызова функции"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        logger.info(f"Вызвана функция: {func.__name__}")
        result = func(*args, **kwargs)
        logger.info(f"Функция {func.__name__} завершена")
        return result
    return wrapper
def counter_decorator(func):
    """Декоратор для подсчета количества вызовов функции"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.count += 1
        logger.info(f"Функция {func.__name__} вызвана {wrapper.count} раз(а)")
        result = func(*args, **kwargs)

def style_decorator(func):
    """Декоратор для изменения стиля кнопки после нажатия."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = 