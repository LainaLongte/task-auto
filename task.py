import xlrd


class Task:
    def __init__(self, inst, parameter, retry: int):
        self.inst = inst
        self.parameter = parameter
        self.retry = retry

    @staticmethod
    def read_excel_to_objects(excel_name):
        # 打开Excel文件
        workbook = xlrd.open_workbook(excel_name)
        # 选择第一个工作表（假设为名为'Sheet1'的工作表）
        sheet = workbook.sheet_by_index(0)
        # 获取工作表的行数
        num_rows = sheet.nrows

        # 定义一个列表用于存储转换后的对象
        task_list = []
        # 遍历每一行数据，并将数据转换成对象
        for i in range(1, num_rows):  # 从第2行开始，跳过标题行
            row_data = sheet.row_values(i)
            inst = row_data[0]
            parameter = row_data[1]
            retry = 1 if row_data[2] == '' else int(row_data[2])

            task_item = Task(inst, parameter, retry)
            task_list.append(task_item)

        return task_list


if __name__ == '__main__':

    excel_name = 'cmd.xls'
    tasks = Task.read_excel_to_objects(excel_name)

    # 打印转换后的任务实例对象列表
    print()
    for task in tasks:
        print(f"指令：{task.inst}, 参数：{task.parameter}, 重试次数：{task.retry}")
