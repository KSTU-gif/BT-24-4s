from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton,
    QVBoxLayout, QHBoxLayout, QComboBox, QLineEdit
)
from PyQt5.QtCore import QTimer, Qt
import sys


class TimerApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Таймер и секундомер")
        self.resize(300, 200)

        self.time_label = QLabel("00:00")
        self.time_label.setAlignment(Qt.AlignCenter)

        self.start_btn = QPushButton("Start")
        self.stop_btn = QPushButton("Stop")

        self.mode_box = QComboBox()
        self.mode_box.addItems([
            "Секундомер",
            "Отсчёт вниз"
        ])

        self.interval_input = QLineEdit()
        self.interval_input.setPlaceholderText("Интервал (сек)")

        self.timer = QTimer()
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.update_time)

        self.seconds = 0

        layout = QVBoxLayout()

        layout.addWidget(self.time_label)
        layout.addWidget(self.mode_box)
        layout.addWidget(self.interval_input)

        button_layout = QHBoxLayout()
        button_layout.addWidget(self.start_btn)
        button_layout.addWidget(self.stop_btn)
        layout.addLayout(button_layout)

        self.setLayout(layout)

        self.start_btn.clicked.connect(self.start)
        self.stop_btn.clicked.connect(self.stop)

    def start(self):
        mode = self.mode_box.currentText()

        if mode == "Секундомер":
            self.seconds = 0

        elif mode == "Отсчёт вниз":
            try:
                self.seconds = int(self.interval_input.text())
            except:
                self.seconds = 0

        self.update_label()
        self.timer.start()

    def stop(self):
        self.timer.stop()

    def update_time(self):
        mode = self.mode_box.currentText()

        if mode == "Секундомер":
            self.seconds += 1

        elif mode == "Отсчёт вниз":
            if self.seconds > 0:
                self.seconds -= 1
            else:
                self.timer.stop()

        self.update_label()

    def update_label(self):
        m = self.seconds // 60
        s = self.seconds % 60
        self.time_label.setText(f"{m:02d}:{s:02d}")


app = QApplication(sys.argv)
window = TimerApp()
window.show()
sys.exit(app.exec_())
