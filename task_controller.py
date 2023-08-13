from task import Task
from inst import Mouse, InstCtrl


class TaskController:

    @staticmethod
    def execute_task(task_script: str):
        tasks = Task.read_excel_to_objects(task_script)
        print()
        if tasks:
            InstCtrl.execute_tasks(tasks)
        else:
            print('输入有误或者已经退出!')


if __name__ == '__main__':
    # # 示例任务列表
    # tasks = [
    #     Task('左键点击', '位置A', 1),
    #     Task('等待', '1', 1),
    #     Task('粘贴文本', 'Hello', 1)
    # ]

    TaskController.execute_task('cmd.xls')
