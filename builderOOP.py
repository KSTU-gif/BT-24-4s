import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QLineEdit, QComboBox
)
from PyQt5.QtGui import QFont


# === Абстрактный строитель ===
class UIBuilder:
    def reset(self):
        raise NotImplementedError

    def add_label(self):
        raise NotImplementedError

    def add_button(self):
        raise NotImplementedError

    def add_text_field(self):
        raise NotImplementedError

    def set_background(self, color):
        raise NotImplementedError

    def get_result(self):
        raise NotImplementedError


# === Конкретный строитель ===
class SimpleUIBuilder(UIBuilder):
    def __init__(self):
        self.reset()

    def reset(self):
        self.window = QWidget()
        self.layout = QVBoxLayout(self.window)
        self.window.setLayout(self.layout)
        self.window.setWindowTitle("Построенное окно")

    def add_label(self):
        lbl = QLabel("Привет! Это метка 😊")
        lbl.setFont(QFont("Arial", 12))
        self.layout.addWidget(lbl)

    def add_button(self):
        btn = QPushButton("Кнопка действия")
        btn.setFont(QFont("Arial", 11))
        self.layout.addWidget(btn)

    def add_text_field(self):
        txt = QLineEdit()
        txt.setPlaceholderText("Введите текст...")
        self.layout.addWidget(txt)

    def set_background(self, color):
        self.window.setStyleSheet(f"background-color: {color};")

    def get_result(self):
        return self.window


# === Директор (управляет строительством) ===
class UIDirector:
    def __init__(self, builder: UIBuilder):
        self.builder = builder

    def build_minimal_ui(self, color):
        self.builder.reset()
        self.builder.set_background(color)
        self.builder.add_label()

    def build_full_ui(self, color):
        self.builder.reset()
        self.builder.set_background(color)
        self.builder.add_label()
        self.builder.add_text_field()
        self.builder.add_button()


# === Главное окно программы ===
class BuilderDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("🎨 Паттерн 'Строитель' — PyQt5")
        self.setGeometry(200, 200, 400, 250)

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        # --- Настройки пользователя ---
        self.mode_box = QComboBox()
        self.mode_box.addItems(["Минимальный интерфейс", "Полный интерфейс"])

        self.color_box = QComboBox()
        self.color_box.addItems(["white", "lightblue", "lightgreen", "#f0e68c", "#222"])

        self.build_button = QPushButton("Построить интерфейс")
        self.build_button.clicked.connect(self.build_ui)

        self.layout.addWidget(QLabel("Выбери тип интерфейса:"))
        self.layout.addWidget(self.mode_box)
        self.layout.addWidget(QLabel("Выбери цвет фона:"))
        self.layout.addWidget(self.color_box)
        self.layout.addWidget(self.build_button)

    def build_ui(self):
        builder = SimpleUIBuilder()
        director = UIDirector(builder)

        mode = self.mode_box.currentText()
        color = self.color_box.currentText()

        if mode == "Минимальный интерфейс":
            director.build_minimal_ui(color)
        else:
            director.build_full_ui(color)

        window = builder.get_result()
        window.show()


# === Запуск приложения ===
if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = BuilderDemo()
    demo.show()
    sys.exit(app.exec_())
