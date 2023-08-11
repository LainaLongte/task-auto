import time
import pyautogui
import pyperclip

from task import Task

# 指令表
instruction_table = {
    '点击': 1,
    '点击2': 2,
    '点击右': 3,
    '滚轮': 4,
    '等待': 5,
    '输入文本': 6,
    'hotkey': 7
}


class TaskService:
    # 方法执行任务列表
    @staticmethod
    def execute_tasks(tasks,retry=2):
        i = 1
        while i < retry:
            for task_item in tasks:
                TaskService.execute_task(task_item)
            i += 1

    # 方法执行任务项，查询指令表，执行对应指令
    @staticmethod
    def execute_task(task:Task):
        instruction_type = task.inst
        instruction_code = instruction_table.get(instruction_type)

        if instruction_code is None:
            print(f"未知的指令类型: {instruction_type}")
            return

        # 执行对应指令操作
        if instruction_code == 1:
            print("执行左键点击操作")
            # 添加执行左键点击操作的代码
            Mouse.click_with_retry(task)
        elif instruction_code == 2:
            print("执行左键双击操作")
            # 添加执行左键双击操作的代码
            Mouse.click_with_retry(task, 2)
        elif instruction_code == 3:
            print("执行右键点击操作")
            # 添加执行右键点击操作的代码
            Mouse.click_with_retry(task, button="right")
        elif instruction_code == 4:
            print("执行滚轮滑动操作")
            # 添加执行滚轮滑动操作的代码
            pyautogui.hotkey(int(task.parameter))
            print(f"滚轮滑动{task.parameter}px")
        elif instruction_code == 5:
            print("执行等待操作")
            # 添加执行等待操作的代码
            time.sleep(task.parameter)
        elif instruction_code == 6:
            print("执行粘贴文本操作")
            # 添加执行粘贴文本操作的代码
            pyperclip.copy(task.parameter)
            pyautogui.hotkey('ctrl', 'v')
            time.sleep(0.5)
            print("输入:", task.parameter)
        elif instruction_code == 7:
            print("执行快捷键操作")
            # 添加执行快捷键操作的代码
            key_value = tuple(task.parameter.split('+'))
            pyautogui.hotkey(*key_value)
            time.sleep(0.5)
            print("输入:", task.parameter)

        else:
            print(f"未知的指令代码: {instruction_code}")


class Mouse:
    @staticmethod
    def get_cursor_location(image_name):
        cursor_location = pyautogui.locateCenterOnScreen(image_name, confidence=0.9)
        return cursor_location

    @staticmethod
    def click_with_retry(t: Task, clicks=1, button="left"):
        retry = t.retry
        while True:
            cursor = Mouse.get_cursor_location(t.parameter)
            if cursor is not None:
                pyautogui.click(cursor.x, cursor.y, clicks=clicks, interval=0.2, duration=0.2, button=button)
                if retry > 1:
                    print(f"继续执行{retry - 1}次")
                    retry -= 1
                elif retry < 1:
                    continue  # 继续无限重试
                else:
                    break
            print("未找到匹配图片,0.1秒后重试")
            time.sleep(0.1)


# 示例：初始化鼠标光标位置并执行左键点击
if __name__ == '__main__':
    # 示例任务列表
    task1 = Task('点击', 'user_ico.png', 1)
    task2 = Task('点击2', 'user_ico.png', 1)
    task3 = Task('点击右', 'user_ico.png', 1)
    task4 = Task('滚轮', 'user_ico.png', 1)
    task5 = Task('等待', 'user_ico.png', 1)
    task6 = Task('输入文本', 'user_ico.png', 1)
    task7 = Task('键盘', 'user_ico.png', 1)

    print(instruction_table)
    # 执行任务
    Mouse.click_with_retry(task1)
    Mouse.click_with_retry(task2, 2)
    Mouse.click_with_retry(task3, button="right")
