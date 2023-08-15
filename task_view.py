from PySide2.QtWidgets import QApplication, QMainWindow, QPushButton, QPlainTextEdit


class TaskView:
    def __init__(self):
        self.app = QApplication([])

        self.window = QMainWindow()
        self.window.move(300, 300)
        self.window.resize(500, 400)
        self.window.setWindowTitle('任务控制台')

        self.textEdit = QPlainTextEdit(self.window)
        self.textEdit.move(10, 25)
        self.textEdit.resize(300, 350)

        self.button = QPushButton('执行任务', self.window)
        self.button.move(380, 80)
        # 连接按钮的点击事件到槽函数
        self.button.clicked.connect(self.exec_task)

        self.window.show()
        self.app.exec_()

    @staticmethod
    def exec_task():
        print("任务执行中...")
        # TaskController.execute_task('cmd.xls')


task_view = TaskView()
