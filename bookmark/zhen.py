def map_frame_rate(frame_rate):
    min_frame_rate = 0  # 帧率范围最小值
    max_frame_rate = 999  # 帧率范围最大值

    min_target_value = 0  # 目标范围最小值
    max_target_value = 23  # 目标范围最大值

    # 使用线性映射计算转换后的值
    mapped_value = ((frame_rate - min_frame_rate) / (max_frame_rate - min_frame_rate)) * (
            max_target_value - min_target_value) + min_target_value
    return round(mapped_value)


# 在这里替换成您的帧率值
original_frame_rate = 83

mapped_frame_rate = map_frame_rate(83)
print("映射后的帧率（四舍五入）:", mapped_frame_rate)
