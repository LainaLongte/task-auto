import time
import pyautogui
import pyperclip

from task import Task


class InstructionExecutor:
    @staticmethod
    def execute_click(task: Task, button="left", clicks=1):
        Mouse.execute_click(task, button=button, clicks=clicks)

    @staticmethod
    def execute_scroll(task: Task):
        try:
            pyautogui.scroll(int(task.parameter))
            print(f"滚轮滑动{task.parameter}px")
        except Exception as e:
            print(f"滚轮滑动操作失败: {e}")

    @staticmethod
    def execute_wait(task: Task):
        try:
            time.sleep(task.parameter)
            print(f"等待{task.parameter}秒")
        except Exception as e:
            print(f"等待操作失败: {e}")

    @staticmethod
    def execute_input_text(task: Task):
        try:
            pyperclip.copy(task.parameter)
            pyautogui.hotkey('ctrl', 'v')
            time.sleep(0.5)
            print("输入文本:", task.parameter)
        except Exception as e:
            print(f"输入文本操作失败: {e}")

    @staticmethod
    def execute_hotkey(task: Task):
        try:
            key_value = tuple(task.parameter.split('+'))
            pyautogui.hotkey(*key_value)
            time.sleep(0.5)
            print("执行快捷键操作:", task.parameter)
        except Exception as e:
            print(f"快捷键操作失败: {e}")


class Mouse:
    @staticmethod
    def get_cursor_location(image_name):
        try:
            cursor_location = pyautogui.locateCenterOnScreen(image_name, confidence=0.9)
            return cursor_location
        except pyautogui.ImageNotFoundException:
            # 如果找不到图像
            return None
        except Exception as e:
            # 其他异常情况
            print(f"获取光标位置失败: {e}")
            return None

    @staticmethod
    def execute_click(t: Task, clicks=1, button="left"):
        retry = t.retry
        while True:
            cursor = Mouse.get_cursor_location(t.parameter)
            if cursor is not None:
                try:
                    pyautogui.click(cursor[0], cursor[1], clicks=clicks, interval=0.2, duration=0.2, button=button)
                    if retry > 1:
                        print(f"继续执行{retry - 1}次")
                        retry -= 1
                    elif retry < 1:
                        continue  # 继续无限重试
                    else:
                        break
                except Exception as e:
                    print(f"点击操作失败: {e}")
            print("未找到匹配图片,0.1秒后重试")
            time.sleep(0.1)


class InstCtrl:
    @staticmethod
    def check_task(task: Task):
        return None

    @staticmethod
    def execute_tasks(tasks):
        for task_item in tasks:
            InstCtrl.execute_task(task_item)

    @staticmethod
    def execute_task(task):
        instruction_type = task.inst
        instruction_executor = InstructionExecutor()

        if instruction_type == '点击':
            instruction_executor.execute_click(task)
        elif instruction_type == '点击2':
            instruction_executor.execute_click(task, clicks=2)
        elif instruction_type == '点击右':
            instruction_executor.execute_click(task, button="right")
        elif instruction_type == '滚轮':
            instruction_executor.execute_scroll(task)
        elif instruction_type == '等待':
            instruction_executor.execute_wait(task)
        elif instruction_type == '输入文本':
            instruction_executor.execute_input_text(task)
        elif instruction_type == '热键':
            instruction_executor.execute_hotkey(task)
        else:
            print(f"未知的指令类型: {instruction_type}")


# 示例：初始化鼠标光标位置并执行左键点击
if __name__ == '__main__':
    task_path = './task/'
    # 示例任务列表
    task1 = Task('点击', task_path+'16g.png', 1)
    task2 = Task('点击2', task_path+'签到.png', 1)
    task3 = Task('点击右', task_path+'user_ico.png', 1)
    task4 = Task('滚轮', task_path+'分享.png', 1)
    task5 = Task('等待', 1, 1)
    task6 = Task('输入文本', 'abc', 1)
    task7 = Task('键盘', 'win+d', 1)

    InstCtrl.execute_task(task1)
