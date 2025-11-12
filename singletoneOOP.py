import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout


# === Одиночка ===
class SettingsManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(SettingsManager, cls).__new__(cls)
            cls._instance.theme = "Light"
            cls._instance.language = "Русский"
        return cls._instance


# === Главное окно ===
class SingletonDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("🔁 Паттерн 'Одиночка' — PyQt5")
        self.setGeometry(200, 200, 400, 250)

        layout = QVBoxLayout()
        self.setLayout(layout)

        self.manager = SettingsManager()

        self.label = QLabel(f"Текущая тема: {self.manager.theme}")
        self.label_lang = QLabel(f"Язык: {self.manager.language}")

        layout.addWidget(self.label)
        layout.addWidget(self.label_lang)

        self.btn_change = QPushButton("Изменить настройки")
        self.btn_change.clicked.connect(self.change_settings)
        layout.addWidget(self.btn_change)

        self.btn_check = QPushButton("Открыть другое окно (тот же Singleton)")
        self.btn_check.clicked.connect(self.open_another_window)
        layout.addWidget(self.btn_check)

    def change_settings(self):
        manager = SettingsManager()
        manager.theme = "Dark"
        manager.language = "English"

        self.label.setText(f"Текущая тема: {manager.theme}")
        self.label_lang.setText(f"Язык: {manager.language}")

    def open_another_window(self):
        # Это второе окно, но использует тот же экземпляр менеджера
        another = AnotherWindow()
        another.show()


class AnotherWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Второе окно — проверка Singleton")
        self.setGeometry(650, 200, 300, 150)

        layout = QVBoxLayout()
        self.setLayout(layout)

        manager = SettingsManager()
        layout.addWidget(QLabel(f"Тема: {manager.theme}"))
        layout.addWidget(QLabel(f"Язык: {manager.language}"))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SingletonDemo()
    window.show()
    sys.exit(app.exec_())
