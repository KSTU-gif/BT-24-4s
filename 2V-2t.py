from PyQt5.QtWidgets import (
    QApplication, QWidget, QGridLayout,
    QLineEdit, QPushButton, QLabel
)
import sys


class AuthForm(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Авторизация")

        layout = QGridLayout()

        
        self.login = QLineEdit()
        self.login.setPlaceholderText("Логин")

        
        self.password = QLineEdit()
        self.password.setPlaceholderText("Пароль")
        self.password.setEchoMode(QLineEdit.Password)

       
        self.btn_login = QPushButton("Войти")
        self.btn_reg = QPushButton("Регистрация")

       
        self.hint = QLabel("Введите логин и пароль")
        self.hint.setStyleSheet("color: gray;")

       
        layout.addWidget(self.login,     0, 0)
        layout.addWidget(self.btn_reg,   0, 1)

        layout.addWidget(self.password,  1, 0)
        layout.addWidget(self.btn_login, 1, 1)

        layout.addWidget(self.hint,      2, 0, 1, 2)

        self.setLayout(layout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = AuthForm()
    form.show()
    sys.exit(app.exec_())
