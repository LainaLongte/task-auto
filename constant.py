# 定义全局的状态变量和搜索区域常量
current_window = None
SEARCH_REGION = (0, 0, 1920, 1080)
LEI_0 = (18, 0, 941, 540)

# 服务器
service_1 = '尼德霍格.png'
service_2 = '天之锁.png'
service_3 = '时光之刃.png'
service_4 = '命运之线.png'
service_5 = '永恒之枪.png'
service_6 = '奇迹之匣.png'


def set_current_window(window_region):
    global current_window
    current_window = window_region


def get_search_region():
    return current_window
