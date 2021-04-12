import os
from datetime import datetime

import pandas as pd


def list_to_dict(list_):
    """
    返回：{元素:[元素对应的位置]}
    :param list_: 重复元素的列表。ls = ['a', 'b', 'c', 'a']
    :return: {'a': [0, 3], 'b': [1], 'c': [2]}
    """
    dict_ = {}
    for value in list_:
        dict_[value] = []
    for index, value in enumerate(list_):
        dict_[value].append(index)
    return dict_


def find_closest_time(df, indexes, subway_time):
    # 在df的indexes这些行中，找到与subway_time最接近的时间，并返回这一行的index
    now_index = None
    for index in indexes:
        row = df.iloc[index, :]
        bus_time = datetime.strptime(row[3], "%H:%M:%S")
        if subway_time < bus_time:
            now_close_time = bus_time  # 初始假设的最接近的时间
            break

    for index in indexes:
        row = df.iloc[index, :]
        bus_time = datetime.strptime(row[3], "%H:%M:%S")
        if subway_time < bus_time <= now_close_time:  # 找到一个距离更近的时间
            now_close_time = bus_time
            now_index = index

    return now_index


def find_indexes(bus_dict_, card_id):
    # 从df4中找idCard，返回index列表，没找到返回空列表
    # 先建立哈希表

    if card_id in bus_dict_.keys():
        return bus_dict_[card_id]
    else:
        return []


def save(file, row_subway, row_bus):
    """
    :param file: 保存到的文件地址
    :param row_subway: 地铁下车的行信息
    :param row_bus: 公交上车的行信息
    :return:
    """
    dict_ = {
        '卡号': [row_subway[0]],
        '地铁卡种': [row_subway[1]],
        '地铁交易日期': [row_subway[2]],
        '地铁交易时间': [row_subway[3]],
        '地铁商户名称': [row_subway[4]],
        '地铁进出站': [row_subway[5]],
        '地铁机具编号': [row_subway[6]],
        '地铁线路编号': [row_subway[7]],
        '地铁车辆编号': [row_subway[8]],
        '地铁站点编号': [row_subway[9]],
        '地铁站名称': [row_subway[10]],

        '公交卡种': [row_bus[1]],
        '公交交易日期': [row_bus[2]],
        '公交交易时间': [row_bus[3]],
        '公交商户名称': [row_bus[4]],
        '公交进出站': [row_bus[5]],
        '公交机具编号': [row_bus[6]],
        '公交线路编号': [row_bus[7]],
        '公交车辆编号': [row_bus[8]],
        '公交线路': [row_bus[9]]
    }
    df = pd.DataFrame(dict_)

    if not os.path.exists(file):
        df.to_csv(file, mode='w', header=True, index=False)
    else:
        df.to_csv(file, mode='a', header=False, index=False)
