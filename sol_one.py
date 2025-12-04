from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget, QMessageBox

import sys

from random import randint

class AppState(object):
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.counter = 0
        return cls._instance
  
    def inc(self):
        self.counter += 1

    def get(self):
        return self.counter

class AnotherWindow(QWidget):
    """
    This "window" is a QWidget. If it has no parent, it
    will appear as a free-floating window as we want.
    """
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()

        s = AppState()

        self.label = QLabel(f"Counter: {s.get()}")
        layout.addWidget(self.label)
        self.setLayout(layout)


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.button = QPushButton('Нажми меня', self)
        self.button.clicked.connect(self.show_new_window)

        # Создаем вертикальный layout и добавляем кнопку
        layout = QVBoxLayout()
        layout.addWidget(self.button)

        # Устанавливаем layout для основного окна
        self.setLayout(layout)

        # Настройки окна
        self.setWindowTitle('PyQt5 Пример')
        self.setGeometry(300, 300, 300, 200)
    

    def show_new_window(self):
        s = AppState()
        s.inc()

app = QApplication(sys.argv)
w = MainWindow()
w.show()
v = AnotherWindow()
v.show()
app.exec()