import sys
import copy
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel


# === Прототип кнопки ===
class ButtonPrototype:
    def __init__(self, text, color):
        self.text = text
        self.color = color

    def clone(self):
        # Возвращаем копию (глубокое копирование)
        return copy.deepcopy(self)

    def create_button(self):
        btn = QPushButton(self.text)
        btn.setStyleSheet(f"background-color: {self.color}; color: white; border-radius: 6px; padding: 5px;")
        return btn


# === Главное окно ===
class PrototypeDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("🧬 Паттерн 'Прототип' — PyQt5")
        self.setGeometry(200, 200, 400, 250)

        layout = QVBoxLayout()
        self.setLayout(layout)

        self.label = QLabel("Создание кнопок-клонов:")
        layout.addWidget(self.label)

        # Оригинал
        self.prototype = ButtonPrototype("Оригинал", "blue")

        # Оригинальная кнопка
        btn_original = self.prototype.create_button()
        layout.addWidget(btn_original)

        # Клонированные кнопки
        clone1 = self.prototype.clone()
        clone1.text = "Клон 1"
        clone1.color = "green"

        clone2 = self.prototype.clone()
        clone2.text = "Клон 2"
        clone2.color = "red"

        layout.addWidget(clone1.create_button())
        layout.addWidget(clone2.create_button())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PrototypeDemo()
    window.show()
    sys.exit(app.exec_())
