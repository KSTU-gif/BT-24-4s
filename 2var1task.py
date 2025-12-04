from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QPlainTextEdit, QVBoxLayout, QLabel, QFrame
from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QColor, QRegExpValidator, QSyntaxHighlighter, QTextCharFormat
from PyQt5.Qt import *
import sys

class SyntaxHighlighter(QSyntaxHighlighter):
    def __init__(self, parnet):
        super().__init__(parnet)
        self._highlight_lines = {}

    def highlight_line(self, line_num, fmt):
        if isinstance(line_num, int) and line_num >= 0 and isinstance(fmt, QTextCharFormat):
            self._highlight_lines[line_num] = fmt
            block = self.document().findBlockByLineNumber(line_num)
            self.rehighlightBlock(block)

    def clear_highlight(self):
        self._highlight_lines = {}
        self.rehighlight()

    def highlightBlock(self, text):
        blockNumber = self.currentBlock().blockNumber()
        fmt = self._highlight_lines.get(blockNumber)
        if fmt is not None:
            self.setFormat(0, len(text), fmt)

class AppDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(1200, 800)

        mainLayout = QVBoxLayout()

        validator = QRegExpValidator(QRegExp(r'[0-9 ]+'))

        self.lineEdit = QLineEdit()
        self.lineEdit.setStyleSheet('font-size: 30px; height: 50px;')
        self.lineEdit.setValidator(validator)
        self.lineEdit.textChanged.connect(self.onTextChanged)
        mainLayout.addWidget(self.lineEdit)

        self.textEditor = QPlainTextEdit()
        self.textEditor.setStyleSheet('font-size: 30px; color: green')
        mainLayout.addWidget(self.textEditor)

        for i in range(1, 21):
            self.textEditor.appendPlainText('Line {0}'.format(i))

        self.highlighter = SyntaxHighlighter(self.textEditor.document())
        self.setLayout(mainLayout)

    def onTextChanged(self, text):
        fmt = QTextCharFormat()
        fmt.setBackground(QColor('yellow'))

        self.highlighter.clear_highlight()

        try:
            lineNumber = int(text) - 1
            self.highlighter.highlight_line(lineNumber, fmt)
        except ValueError:
            pass

    def open_second_window(self):
        self.second_window = MainWindow(self)
        self.second_window.show()

class SecondWindow(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Второе окно")
        self.setGeometry(400, 100, 300, 200)

        layout = QVBoxLayout()
        self.label = QLabel("Это второе окно")
        layout.addWidget(self.label)
        self.setLayout(layout)

app = QApplication(sys.argv)        
demo = AppDemo()
demo.show()
sys.exit(app.exec_())

class MainWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('PyQt QLineEdit Widget')
        self.setGeometry(100, 100, 320, 210)

        password = QLineEdit(self, echoMode=QLineEdit.EchoMode.Password)

        # place the widget on the window
        layout = QVBoxLayout()
        layout.addWidget(password)
        self.setLayout(layout)

        # show the window
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())

class WindowInputName(QtWidgets.QWidget):
    def __init__(self):
        super(WindowInputName, self).__init__()

        self.setUpui()
        self.setForm()

    def setUpui(self):
        self.resize(320, 320)
        self.setWindowTitle("Программа")
        self.setStyleSheet('background-color: #3f5664;')
        self.fram = QFrame()
        self.fram.setFixedSize(300, 300)
        self.fram.setStyleSheet('''QFrame {
        background-color: #2b3942;
        border-radius: 30px;
        }''')
        shadow = QGraphicsDropShadowEffect(blurRadius=70, xOffset=-10, yOffset=10, color=QColor('#97abb5'))
        self.fram.setGraphicsEffect(shadow)

        self.user_input = QLineEdit()
        self.user_input_2 = QLineEdit()

        form_layout = QtWidgets.QFormLayout(self.fram)
        form_layout.addRow(
            QLabel('<h2 style="color: #A05344;">User input:<h3>'), 
            self.user_input
        )
        form_layout.addRow('User input2 :', self.user_input_2)
        form_layout.setFormAlignment(QtCore.Qt.AlignCenter)

    def setForm(self):
        hbox = QtWidgets.QHBoxLayout(self)
        hbox.addWidget(self.fram)
        self.setLayout(hbox)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    win = WindowInputName()
    win.show()
    sys.exit(app.exec_())