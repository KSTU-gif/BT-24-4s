import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QComboBox
)

from PyQt5.QtGui import QFont, QColor, QPalette

# === Абстрактные классы ===
class AbstractButton:
    def create_button(self, text: str):
        raise NotImplementedError

class AbstractLabel:
    def create_label(self, text: str):
        raise NotImplementedError
    
class AbstractWidgetFactory:
    def create_button(self):
        raise NotImplementedError

    def create_label(self):
        raise NotImplementedError
    
# === Конкретные фабрики ===
class LightWidgetFactory(AbstractWidgetFactory):
    def create_button(self):
        return LightButton()
    
    def create_label(self):
        return LightLabel()
    
class DarkWidgetFactory(AbstractWidgetFactory):
    def create_button(self):
        return DarkButton()

    def create_label(self):
        return DarkLabel()



# === Конкретные продукты ===
class LightButton(AbstractButton):
    def create_button(self, text):
        btn = QPushButton(text)
        btn.setStyleSheet("background-color: white; color: black; border: 1px solid gray;")
        btn.setFont(QFont("Arial", 11))
        return btn
    
class DarkButton(AbstractButton):
    def create_button(self, text):
        btn = QPushButton(text)
        btn.setStyleSheet("background-color: #333; color: white; border: 1px solid #555;")
        btn.setFont(QFont("Arial", 11))
        return btn


class LightLabel(AbstractLabel):
    def create_label(self, text):
        lbl = QLabel(text)
        lbl.setStyleSheet("color: black;")
        lbl.setFont(QFont("Arial", 11))
        return lbl


class DarkLabel(AbstractLabel):
    def create_label(self, text):
        lbl = QLabel(text)
        lbl.setStyleSheet("color: white;")
        lbl.setFont(QFont("Arial", 11))
        return lbl
    

# === Главное окно ===
class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("🎨 Абстрактная фабрика PyQt")
        self.setGeometry(200, 200, 400, 250)

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.theme_selector = QComboBox()
        self.theme_selector.addItems(["Light", "Dark"])
        self.theme_selector.currentTextChanged.connect(self.change_theme)
        self.layout.addWidget(self.theme_selector)

        self.factory = None
        self.update_ui("Light")

    def change_theme(self, theme_name):
        self.update_ui(theme_name)

    def update_ui(self, theme_name):
        # Очистим старые элементы
        for i in reversed(range(1, self.layout.count())):
            widget = self.layout.itemAt(i).widget()
            if widget:
                widget.deleteLater()

        # Создание фабрики
        if theme_name == "Light":
            self.factory = LightWidgetFactory()
            self.setStyleSheet("background-color: white;")
        else:
            self.factory = DarkWidgetFactory()
            self.setStyleSheet("background-color: #222;")

        # Создаём элементы из фабрики
        label = self.factory.create_label().create_label("Это пример лейбла")
        button = self.factory.create_button().create_button("Нажми меня")

        self.layout.addWidget(label)
        self.layout.addWidget(button)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())