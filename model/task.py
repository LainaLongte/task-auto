import xlrd


class Script:
    def __init__(self, name: str, path: str):
        self.name = name
        self.path = path


class Task:
    def __init__(self, inst, parameter, retry: int):
        self.inst = inst
        self.parameter = parameter
        self.retry = retry

    # 打开Excel文件
    # 选择第一个工作表
    # 获取工作表的行数
    # 定义一个列表用于存储转换后的对象
    # 遍历每一行数据，并将数据转换成对象
    # 如果指令是点击，图片加脚本路径
    @staticmethod
    def from_excel(script: Script):
        excel_file = script.path + script.name
        sheet = xlrd.open_workbook(excel_file).sheet_by_index(0)
        num_rows = sheet.nrows

        task_list = []
        for i in range(1, num_rows):  # 从第2行开始，跳过标题行
            row_data = sheet.row_values(i)
            inst = row_data[0]
            parameter = row_data[1] if '点击' not in inst else script.path + row_data[1]
            retry = 1 if row_data[2] == '' else int(row_data[2])

            task_item = Task(inst, parameter, retry)
            task_list.append(task_item)

        return task_list


excel_name = 'task/cmd.xls'

if __name__ == '__main__':

    cmd = Script('sw.xls', '../task/')
    service = Script('service.xls', '../task/service/')

    tasks = Task.from_excel(service)

    # 打印转换后的任务实例对象列表
    print()
    for task in tasks:
        print(f"指令：{task.inst}, 参数：{task.parameter}, 重试次数：{task.retry}")
