import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QPushButton, QVBoxLayout, QWidget


class TextApp:
    def __init__(self):
        self.app = QApplication([])

        self.window = QMainWindow()
        self.window.move(300, 300)
        self.window.resize(500, 400)
        self.window.setWindowTitle('文本框应用')

        self.textEdit = QTextEdit(self.window)
        self.textEdit.move(10, 25)
        self.textEdit.resize(300, 350)

        self.button = QPushButton('执行命令', self.window)
        self.button.move(380, 80)
        self.button.clicked.connect(self.exec_command)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.textEdit)
        self.layout.addWidget(self.button)

        self.central_widget = QWidget()
        self.central_widget.setLayout(self.layout)
        self.window.setCentralWidget(self.central_widget)

        self.window.show()
        self.app.exec_()

    def exec_command(self):
        input_text = self.textEdit.toPlainText().strip()
        output_text = self.process_command(input_text)
        self.textEdit.append("\n> " + input_text)
        self.textEdit.append(output_text)

    @staticmethod
    def process_command(command):
        # Replace with your command processing logic
        if command == "hello":
            return "Hello, world!"
        else:
            return "Unknown command"


text_app = TextApp()
