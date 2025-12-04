from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QComboBox,
    QLineEdit
)
from PyQt5.QtCore import Qt
from abc import ABC, abstractmethod
import sys




class HighlightLineEdit(QLineEdit):
    def __init__(self):
        super().__init__()
        self.setPlaceholderText("Подсветка при вводе")
        self.setStyleSheet("""
            QLineEdit {
                border: 1px solid #888;
                padding: 4px;
            }
            QLineEdit:focus {
                border: 2px solid #4caf50;
                background: #e8f5e9;
            }
        """)


class PasswordLineEdit(QLineEdit):
    def __init__(self):
        super().__init__()
        self.setPlaceholderText("Пароль")
        self.setEchoMode(QLineEdit.Password)


class FramedLineEdit(QLineEdit):
    def __init__(self):
        super().__init__()
        self.setPlaceholderText("Введите текст")
        self.setStyleSheet("border: 2px solid #1976d2; padding: 4px;")




class LineEditCreator(ABC):
    @abstractmethod
    def create_line_edit(self):
        pass


class HighlightCreator(LineEditCreator):
    def create_line_edit(self):
        return HighlightLineEdit()


class PasswordCreator(LineEditCreator):
    def create_line_edit(self):
        return PasswordLineEdit()


class FramedCreator(LineEditCreator):
    def create_line_edit(self):
        return FramedLineEdit()



class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Фабрика LineEdit")

        self.layout = QVBoxLayout()

       
        self.selector = QComboBox()
        self.selector.addItems(["Highlight", "Password", "Framed"])
        self.selector.currentTextChanged.connect(self.recreate_field)

        self.layout.addWidget(self.selector)

       
        self.field = None
        self.recreate_field("Highlight")

        self.setLayout(self.layout)

    def recreate_field(self, type_name):
        if self.field:
            self.layout.removeWidget(self.field)
            self.field.deleteLater()

        if type_name == "Highlight":
            creator = HighlightCreator()
        elif type_name == "Password":
            creator = PasswordCreator()
        else:
            creator = FramedCreator()

        self.field = creator.create_line_edit()
        self.layout.addWidget(self.field)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())
