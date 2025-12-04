#1 вариант
import sys
from PyQt5.QtWidgets import (
	QApplication, QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QLineEdit, QLabel, QGroupBox
)

class BaseButton(QPushButton):
    """Базовый класс кнопки с текстом."""
    def __init__(self,text):
        super().__init__(text)
        
class DangerButton(BaseButton):
    """Красная опасная кнопка."""
    def __init__(self):
        super().__init__("Опасная кнопка")
        self.setStyleSheet("background: #d9534f; color: white;")
        
class SuccessButton(BaseButton):
    """Зеленая кнопка успеха."""
    def __init__(self):
        super().__init__("Успех")
        self.setStyleSheet("background: #5cb85c; color: white;")
        
class DefaultButton(BaseButton):
    """Обычная Кнопка."""
    def __init__(self):
        super().__init__("Обычная кнопка")
        self.setStyleSheet("background: #5cb85c; color: white;")
        
def button_factory(button_type, text):
    if button_type == "Опасная":
        return DangerButton(text or "Опасная Кнопка")
    elif button_type == "Успех":
        return SuccessButton(text or "Успех")
    else:
        return DefaultButton(text or "Обычная Кнопка")
    
class MainWindow(Qwidget):
    def __init__(self):
        super().__init__()
        self.set

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MainWindow()
    window.show()
    app.exec()
