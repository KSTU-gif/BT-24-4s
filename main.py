

# ------------------------ КОНТРОЛЬНАЯ РАБОТА №2 PYQT --------------------------------------


# ----------------  1 ЗАДАНИЕ -----------------------------
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout


class FormBuilder:
    def __init__(self):
        self.widget = QWidget()
        self.layout = QVBoxLayout()
        self.widget.setLayout(self.layout)

    def add_title(self, text):
        label = QLabel(text)
        self.layout.addWidget(label)
        return self

    def add_input(self, placeholder):
        line = QLineEdit()
        line.setPlaceholderText(placeholder)
        self.layout.addWidget(line)
        return self

    def add_button(self, text):
        btn = QPushButton(text)
        self.layout.addWidget(btn)
        return self

    def build(self):
        return self.widget


class LoginFormDirector:
    def __init__(self, builder):
        self.builder = builder

    def construct(self):
        return (
            self.builder
            .add_title("Вход")
            .add_input("Логин или Email")
            .add_input("Пароль")
            .add_button("Войти")
            .build()
        )


class RegisterFormDirector:
    def __init__(self, builder):
        self.builder = builder

    def construct(self):
        return (
            self.builder
            .add_title("Регистрация")
            .add_input("Имя")
            .add_input("Email")
            .add_input("Пароль")
            .add_button("Создать аккаунт")
            .build()
        )


class Main(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Builder Pattern PyQt5")

        layout = QVBoxLayout()

        login_form = LoginFormDirector(FormBuilder()).construct()
        register_form = RegisterFormDirector(FormBuilder()).construct()

        layout.addWidget(login_form)
        layout.addWidget(register_form)

        self.setLayout(layout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())



# ---------------------- 2 ЗАДАНИЕ --------------------------



from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLineEdit, QComboBox,
    QCalendarWidget, QPushButton, QLabel, QMessageBox
)
from PyQt5.QtCore import QDate
import random
import sys


class TaskApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Список задач")
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)


        self.task_input = QLineEdit()
        self.task_input.setPlaceholderText("Введите задачу...")
        self.layout.addWidget(self.task_input)

        
        self.types = ["Работа", "Учёба", "Личное", "Срочно", "Позвонить"]
        random.shuffle(self.types)

        self.type_box = QComboBox()
        self.type_box.addItems(self.types)
        self.layout.addWidget(self.type_box)

        
        self.calendar = QCalendarWidget()
        self.layout.addWidget(self.calendar)

        
        self.btn = QPushButton("Добавить")
        self.btn.clicked.connect(self.add_task)
        self.layout.addWidget(self.btn)

        
        self.last_label = QLabel("Последняя добавленная: —")
        self.layout.addWidget(self.last_label)

    def add_task(self):
        task = self.task_input.text().strip()
        task_type = self.type_box.currentText()
        date = self.calendar.selectedDate()

        today = QDate.currentDate()
        if date < today:
            QMessageBox.warning(self, "Ошибка", "Недопустимая дата")
            return

        if task == "":
            QMessageBox.warning(self, "Ошибка", "Введите название задачи")
            return

        text = f"{task} | Тип: {task_type} | Дата: {date.toString('dd.MM.yyyy')}"
        self.last_label.setText(f"Последняя добавленная: {text}")

        self.task_input.clear()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    w = TaskApp()
    w.show()

    sys.exit(app.exec())



