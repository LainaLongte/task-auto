import time
from constant import SEARCH_REGION, set_current_window, LEI_0
from inst import InstCtrl
from model.task import Script, Task


class TaskController:

    @staticmethod
    def execute_task(script: Script):
        start_time = time.time()  # 记录任务开始时间
        tasks = Task.from_excel(script)
        print()
        if tasks:
            InstCtrl.execute_tasks(tasks)
        else:
            print('输入有误或者已经退出!')

        end_time = time.time()  # 记录任务结束时间
        execution_time = end_time - start_time  # 计算任务执行时间

        print(f"任务 {script.name} 完成，用时: {execution_time:.2f} 秒")


if __name__ == '__main__':
    # # 示例任务列表
    # tasks = [
    #     Task('左键点击', '位置A', 1),
    #     Task('等待', '1', 1),
    #     Task('粘贴文本', 'Hello', 1)
    # ]
    set_current_window(SEARCH_REGION)
    sw = Script('sw.xls', 'task/')
    service = Script('service.xls', 'task/service/')
    TaskController.execute_task(sw)
    set_current_window(LEI_0)
    TaskController.execute_task(service)

