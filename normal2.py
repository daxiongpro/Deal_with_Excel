# Time: 2020/4/26-11:44
# Author: Rex
from datetime import datetime

import pandas as pd

file1 = r'C:\Users\Administrator\Desktop\yllCsv\df1.csv'
file2 = r'C:\Users\Administrator\Desktop\yllCsv\df2.csv'
file3 = r'C:\Users\Administrator\Desktop\yllCsv\df3.csv'
file4 = r'C:\Users\Administrator\Desktop\yllCsv\df4.csv'
result = r'C:\Users\Administrator\Desktop\yllCsv\result.csv'

# bus1 = pd.read_csv(file1, encoding='gbk')
# bus2 = pd.read_csv(file2, encoding='gbk')
df3 = pd.read_csv(file3, encoding='gbk')
df4 = pd.read_csv(file4)


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


def find_indexes(card_id):
    # 从df4中找idCard，返回index列表，没找到返回空列表
    # 先建立哈希表
    dic_in_df2 = list_to_dict(df4.iloc[:, 0])
    if card_id in dic_in_df2.keys():
        return dic_in_df2[card_id]
    else:
        return []


def main():
    for index, row in df3.iterrows():
        card_id = row[0]
        # 从df4中找idCard，返回index列表，没找到返回空列表
        indexes_in_df4 = find_indexes(card_id)
        # 在df4中找到了
        if len(indexes_in_df4) != 0:
            for index in indexes_in_df4:
                # 地铁下车时间
                t1 = datetime.strptime(row[3], "%H:%M:%S")
                # 公交上车时间
                t2 = datetime.strptime(df4.iloc[index, 3], "%H:%M:%S")
                #公交时间在地铁时间之后
                if t2 > t1:
                    print('卡号：', row[0],
                          '地铁下车时间：', row[3],
                          '公交上车时间：', df4.iloc[index, 3])
                    break
            else:
                print('卡号：', row[0], '公交上车时间都在地铁时间之前')
        else:
            print('没找到第', index, '行的id', row[0])


if __name__ == '__main__':
    main()
