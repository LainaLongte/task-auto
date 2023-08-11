from task import Task
from task_service import Mouse, TaskService


class TaskController:

    @staticmethod
    def execute_task(task: str):
        tasks = Task.read_excel_to_objects(task)
        print()
        if tasks:
            TaskService.execute_tasks(tasks)
            # key = input('选择功能: 1.做一次 2.循环到死 \n')
            # if key == '1':
            #     TaskService.execute_task_list(tasks)
            # elif key == '2':
            #     while True:
            #         TaskService.execute_task_list(tasks)
            #         time.sleep(0.1)
            #         print("等待0.1秒")
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
