import sys  # sys нужен для передачи argv в QApplication
from PyQt6.QtWidgets import (QWidget, QLineEdit, QPushButton, QApplication, QVBoxLayout)


class Window(QWidget):

    def __init__(self):
        super().__init__()
        self.inputName = QLineEdit(self)
        self.inputEmail = QLineEdit(self)
        self.inputSecondName = QLineEdit(self)
        self.buttonSave = QPushButton(self)
        layout = QVBoxLayout()
        layout.addWidget(self.inputName)
        layout.addWidget(self.inputEmail)
        layout.addWidget(self.inputSecondName)
        layout.addWidget(self.buttonSave)
        
	
def main():
    app = QApplication(sys.argv)  # Новый экземпляр QApplication
    window = Window()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec()  # и запускаем приложение

if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()