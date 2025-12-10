from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton
import sys

class CounterModel:
    def __init__(self):
        self.value = 0
        self.subscribers = []

    def subscribe(self, callback):
        self.subscribers.append(callback)

    def notify(self):
        for callback in self.subscribers:
            callback(self.value)

    def increment(self):
        self.value += 1
        self.notify()


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Observer task")

        layout = QVBoxLayout()

        self.label1 = QLabel("Label 1: 0")
        self.label2 = QLabel("Label 2: 0")

        self.label1.setStyleSheet("""

        """)

        self.button = QPushButton("Увелечить счетчик")

        layout.addWidget(self.label1)
        layout.addWidget(self.label2)
        layout.addWidget(self.button)

        self.setLayout(layout)

        self.model = CounterModel()

        self.model.subscribe(self.update_label1)
        self.model.subscribe(self.update_label2)

        self.button.clicked.connect(self.model.increment)

    def update_label1(self, value):
        self.label1.setText(f"Label 1: {value}")

    def update_label2(self, value):
        self.label2.setText(f"Label 2: {value}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
