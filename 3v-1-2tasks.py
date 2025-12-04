
import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QGroupBox, QGridLayout 
)
from abc import ABC, abstractmethod




class FormProduct(QWidget):
    """Готовый продукт — набор layout и виджетов."""
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout(self)

    def add_widget(self, widget):
        self.layout.addWidget(widget)




class BaseFormBuilder(ABC):
    def __init__(self):
        self.product = FormProduct()

    @abstractmethod
    def add_title(self):
        pass

    @abstractmethod
    def add_inputs(self):
        pass

    @abstractmethod
    def add_controls(self):
        pass

    def get_result(self):
        return self.product


class MiniFormBuilder(BaseFormBuilder):
    def add_title(self):
        title = QLabel("Мини-форма")
        title.setStyleSheet("font-weight: bold;")
        self.product.add_widget(title)

    def add_inputs(self):
        row = QHBoxLayout()
        self.name_edit = QLineEdit()
        self.name_edit.setPlaceholderText("Имя")
        self.age_edit = QLineEdit()
        self.age_edit.setPlaceholderText("Возраст")
        row.addWidget(self.name_edit)
        row.addWidget(self.age_edit)

        container = QWidget()
        container.setLayout(row)
        self.product.add_widget(container)

    def add_controls(self):
        row = QHBoxLayout()
        ok_btn = QPushButton("OK")
        cancel_btn = QPushButton("Отмена")
        row.addWidget(ok_btn)
        row.addWidget(cancel_btn)

        container = QWidget()
        container.setLayout(row)
        self.product.add_widget(container)


class FullFormBuilder(BaseFormBuilder):

    def add_title(self):
        title = QLabel("Расширенная форма")
        title.setStyleSheet("font-size: 16px; font-weight: bold;")
        self.product.add_widget(title)

    def add_inputs(self):
        group = QGroupBox("Данные пользователя")
        v = QVBoxLayout()

        self.name_edit = QLineEdit()
        self.name_edit.setPlaceholderText("Имя")

        self.surname_edit = QLineEdit()
        self.surname_edit.setPlaceholderText("Фамилия")

        self.age_edit = QLineEdit()
        self.age_edit.setPlaceholderText("Возраст")

        v.addWidget(QLabel("Имя:"))
        v.addWidget(self.name_edit)
        v.addWidget(QLabel("Фамилия:"))
        v.addWidget(self.surname_edit)
        v.addWidget(QLabel("Возраст:"))
        v.addWidget(self.age_edit)

        group.setLayout(v)
        self.product.add_widget(group)

    def add_controls(self):
        row = QHBoxLayout()
        save_btn = QPushButton("Сохранить")
        reset_btn = QPushButton("Сброс")
        close_btn = QPushButton("Закрыть")

        row.addWidget(save_btn)
        row.addWidget(reset_btn)
        row.addWidget(close_btn)

        container = QWidget()
        container.setLayout(row)
        self.product.add_widget(container)




class FormDirector:
    def __init__(self, builder: BaseFormBuilder):
        self.builder = builder

    def build_form(self):
        self.builder.add_title()
        self.builder.add_inputs()
        self.builder.add_controls()
        return self.builder.get_result()


class DiscountCalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Калькулятор скидок")

        layout = QGridLayout()

        self.price_edit = QLineEdit()
        self.price_edit.setPlaceholderText("Цена")

        self.discount_edit = QLineEdit()
        self.discount_edit.setPlaceholderText("% скидки")


        self.calc_btn = QPushButton("Посчитать")
        self.calc_btn.clicked.connect(self.calculate)


        self.result_label = QLabel("Результат будет здесь")


        layout.addWidget(self.price_edit,    0, 0)
        layout.addWidget(self.discount_edit, 0, 1)

        layout.addWidget(self.calc_btn,      1, 0)
        layout.addWidget(self.result_label,  1, 1)

        self.setLayout(layout)

    def calculate(self):
        try:
            price = float(self.price_edit.text())
            discount = float(self.discount_edit.text())
            final_price = price * (1 - discount / 100)
            self.result_label.setText(f"Итого: {final_price:.2f}")
        except ValueError:
            self.result_label.setText("Ошибка ввода")


class BuilderDemoWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Строитель сложного окна")

        main_layout = QVBoxLayout()

        
        mini_builder = MiniFormBuilder()
        mini_director = FormDirector(mini_builder)
        mini_form = mini_director.build_form()
        mini_box = QGroupBox("Мини-форма")
        v1 = QVBoxLayout()
        v1.addWidget(mini_form)
        mini_box.setLayout(v1)

       
        full_builder = FullFormBuilder()
        full_director = FormDirector(full_builder)
        full_form = full_director.build_form()
        full_box = QGroupBox("Расширенная форма")
        v2 = QVBoxLayout()
        v2.addWidget(full_form)
        full_box.setLayout(v2)

        main_layout.addWidget(mini_box)
        main_layout.addWidget(full_box)

        self.setLayout(main_layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    builder_demo = BuilderDemoWindow()
    builder_demo.show()

    discount_window = DiscountCalculator()
    discount_window.show()

    sys.exit(app.exec_())

