# Time: 2020/4/27-9:53
# Author: Rex
# Time: 2020/4/26-15:06
# Author: Rex
# Time: 2020/4/26-11:44
# Author: Rex
from datetime import datetime

import pandas as pd

file1 = r'C:\Users\Administrator\Desktop\yllCsv\df1.csv'
file2 = r'C:\Users\Administrator\Desktop\yllCsv\df2.csv'
file3 = r'C:\Users\Administrator\Desktop\yllCsv\df3.csv'
file4 = r'C:\Users\Administrator\Desktop\yllCsv\df4.csv'
result = r'C:\Users\Administrator\Desktop\yllCsv\result.csv'
result2 = r'C:\Users\Administrator\Desktop\yllCsv\result2.csv'

# df1 = pd.read_csv(file1, encoding='gbk')
# df2 = pd.read_csv(file2, encoding='gbk')
# df3 = pd.read_csv(file3, encoding='gbk')
# df4 = pd.read_csv(file4)
df5 = pd.read_csv(result)

first = True


def list_to_dict(lst):
    '''
    :param list: 重复元素的列表。ls = ['a', 'b', 'c', 'a']
    :return: {'a': [0, 3], 'b': [1], 'c': [2]}

    '''
    dic = {}
    for value in lst:
        dic[value] = []
    for index, value in enumerate(lst):
        dic[value].append(index)

    return dic


# dic_in_df2 = list_to_dict(df4.iloc[:, 0])
dic_in_df5 = list_to_dict(df5.iloc[:, 0])


def find_indexes(card_id):
    # 从df4中找idCard，返回index列表，没找到返回空列表
    # 先建立哈希表

    if card_id in dic_in_df2.keys():
        return dic_in_df2[card_id]
    else:
        return []


def save(file, row3, row4):
    '''
    :param file: 保存到的文件地址
    :param row3: 地铁下车的行信息
    :param row4: 公交上车的行信息
    :return:
    '''
    global first
    dic = {
        '卡号': [row3[0]],
        '地铁卡种': [row3[1]],
        '地铁交易日期': [row3[2]],
        '地铁交易时间': [row3[3]],
        '地铁商户名称': [row3[4]],
        '地铁进出站': [row3[5]],
        '地铁机具编号': [row3[6]],
        '地铁线路编号': [row3[7]],
        '地铁车辆编号': [row3[8]],
        '地铁站点编号': [row3[9]],
        '地铁站名称': [row3[10]],

        '公交卡种': [row4[1]],
        '公交交易日期': [row4[2]],
        '公交交易时间': [row4[3]],
        '公交商户名称': [row4[4]],
        '公交进出站': [row4[5]],
        '公交机具编号': [row4[6]],
        '公交线路编号': [row4[7]],
        '公交车辆编号': [row4[8]],
        '公交线路': [row4[9]]
    }
    df = pd.DataFrame(dic)

    if first == True:
        df.to_csv(file, mode='w', header=True, index=False)
        first = False
    else:
        df.to_csv(file, mode='a', header=False, index=False)


def find_close_time_in_df(df, indexes_in_df4, t1):
    flag = False  # 是否找到过一个

    now_index = None
    for index in indexes_in_df4:
        row = df.iloc[index, :]
        # 第一次找到之前比较只需看是否在地铁时间之后
        if flag == False:
            if t1 < datetime.strptime(row[3], "%H:%M:%S"):
                now_close_time = datetime.strptime(row[3], "%H:%M:%S")
                now_index = index
                flag = True
        # 第二次之后的比较，需要与
        else:
            if t1 < datetime.strptime(row[3], "%H:%M:%S") < now_close_time:
                now_close_time = datetime.strptime(row[3], "%H:%M:%S")
                now_index = index

    return now_index


def main(fromIndex):
    global first
    if fromIndex == 0:
        first = True
    else:
        first = False
    for index, row in df3.iterrows():
        if index >= fromIndex:
            card_id = row[0]
            # 从df4中找idCard，返回index列表，没找到返回空列表
            indexes_in_df4 = find_indexes(card_id)
            # 在df4中找到了
            if len(indexes_in_df4) != 0:
                t1 = datetime.strptime(row[3], "%H:%M:%S")
                # 找出在df4中位置为indexes_in_df4的时间与t1最近的那行的index,没找到返回None
                close_index = find_close_time_in_df(df4, indexes_in_df4, t1)
                if close_index != None:
                    save(result, row, df4.iloc[close_index, :])
                    print('第', index, '行写入成功！')
                else:
                    print('卡号：', row[0], '公交上车时间都在地铁时间之前')
                # t2 = datetime.strptime(t2_str, "%H:%M:%S")
                # for index2 in indexes_in_df4:
                #     # 地铁下车时间
                #     t1 = datetime.strptime(row[3], "%H:%M:%S")
                #     # 公交上车时间
                #
                #     t2 = datetime.strptime(df4.iloc[index2, 3], "%H:%M:%S")
                #     # 公交时间在地铁时间之后
                #     if t2 > t1:
                #         save(result, row, df4.iloc[index2, :])
                #         print('第', index, '行写入成功！')
                #         break
                # else:
                #     print('卡号：', row[0], '公交上车时间都在地铁时间之前')
            else:
                print('没找到第', index, '行的id', row[0])


def get_max_index(indexes):
    max_index = indexes[0]
    max_time = datetime.strptime(df5.iloc[indexes[0], 3], "%H:%M:%S")
    for index in indexes:
        time2 = datetime.strptime(df5.iloc[index, 3], "%H:%M:%S")
        if time2 > max_time:
            max_time = time2
            max_index = index
    return max_index


def drop_not_max_index(indexes):
    # global df5
    delete_index = []
    max_index = get_max_index(indexes)
    for index in indexes:
        if index != max_index:
            delete_index.append(index)

    return delete_index


def main2():
    i = 0
    delete_index = []
    for card_id, indexes in dic_in_df5.items():

        if len(indexes) > 1:
            item_delete_index = drop_not_max_index(indexes)

            delete_index.extend(item_delete_index)
        print('第', i, '行处理完毕')
        i += 1

    print(delete_index)
    df = df5.drop(index=delete_index)
    print('开始写入')
    df.to_csv(result2, mode='w', header=True, index=False)


if __name__ == '__main__':
    # main(0)
    print(dic_in_df5)
    print(len(df5))
    print(df5.iloc[27578, :])
    main2()
