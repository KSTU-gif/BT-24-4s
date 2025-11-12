import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QPushButton, QToolButton, QRadioButton,
    QVBoxLayout, QLabel, QComboBox
)
from PyQt5.QtGui import QFont


# === Абстрактная фабрика ===
class ButtonFactory:
    def create_button(self, text):
        raise NotImplementedError


# === Конкретные фабрики ===
class PushButtonFactory(ButtonFactory):
    def create_button(self, text):
        btn = QPushButton(text)
        btn.setStyleSheet("background-color: lightblue; color: black; border-radius: 6px; padding: 5px;")
        btn.setFont(QFont("Arial", 11))
        return btn


class ToolButtonFactory(ButtonFactory):
    def create_button(self, text):
        btn = QToolButton()
        btn.setText(text)
        btn.setStyleSheet("background-color: lightgreen; color: black; border: 1px solid gray; padding: 4px;")
        btn.setFont(QFont("Arial", 10))
        return btn


class RadioButtonFactory(ButtonFactory):
    def create_button(self, text):
        btn = QRadioButton(text)
        btn.setStyleSheet("color: darkred; font-weight: bold;")
        btn.setFont(QFont("Arial", 11))
        return btn


# === Главное окно ===
class FactoryDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("🏭 Паттерн 'Фабричный метод' — PyQt5")
        self.setGeometry(200, 200, 400, 250)

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.label = QLabel("Выберите тип кнопки:")
        self.label.setFont(QFont("Arial", 12))
        self.layout.addWidget(self.label)

        self.type_box = QComboBox()
        self.type_box.addItems(["QPushButton", "QToolButton", "QRadioButton"])
        self.layout.addWidget(self.type_box)

        self.create_btn = QPushButton("Создать кнопку")
        self.create_btn.clicked.connect(self.create_button)
        self.layout.addWidget(self.create_btn)

        self.result_area = QVBoxLayout()
        self.layout.addLayout(self.result_area)

    def create_button(self):
        # Очистим старые кнопки
        while self.result_area.count():
            widget = self.result_area.takeAt(0).widget()
            if widget:
                widget.deleteLater()

        button_type = self.type_box.currentText()

        # Выбор фабрики
        if button_type == "QPushButton":
            factory = PushButtonFactory()
        elif button_type == "QToolButton":
            factory = ToolButtonFactory()
        else:
            factory = RadioButtonFactory()

        # Создание кнопки через фабрику
        button = factory.create_button(f"Это {button_type}")
        self.result_area.addWidget(button)


# === Запуск приложения ===
if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = FactoryDemo()
    demo.show()
    sys.exit(app.exec_())
