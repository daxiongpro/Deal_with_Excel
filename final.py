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

# df1 = pd.read_csv(file1, encoding='gbk')
# df2 = pd.read_csv(file2, encoding='gbk')
df3 = pd.read_csv(file3, encoding='gbk')
df4 = pd.read_csv(file4)

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


def find_indexes(card_id):
    # 从df4中找idCard，返回index列表，没找到返回空列表
    # 先建立哈希表
    dic_in_df2 = list_to_dict(df4.iloc[:, 0])
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
        '地铁交易日期':[row3[2]],
        '地铁交易时间': [row3[3]],
        '地铁商户名称':[row3[4]],
        '地铁进出站':[row3[5]],
        '地铁机具编号':[row3[6]],
        '地铁线路编号': [row3[7]],
        '地铁车辆编号':[row3[8]],
        '地铁站点编号':[row3[9]],
        '地铁站名称':[row3[10]],

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
        df.to_csv(r'C:\Users\Administrator\Desktop\yllCsv\result.csv', mode='w', header=True, index=False)
        first = False
    else:
        df.to_csv(r'C:\Users\Administrator\Desktop\yllCsv\result.csv', mode='a', header=False, index=False)



def main2(fromIndex):
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
                for index2 in indexes_in_df4:
                    # 地铁下车时间
                    t1 = datetime.strptime(row[3], "%H:%M:%S")
                    # 公交上车时间
                    t2 = datetime.strptime(df4.iloc[index2, 3], "%H:%M:%S")
                    # 公交时间在地铁时间之后
                    if t2 > t1:
                        save(result, row, df4.iloc[index2, :])
                        print('第', index, '行写入成功！')
                        break
                else:
                    print('卡号：', row[0], '公交上车时间都在地铁时间之前')
            else:
                print('没找到第', index, '行的id', row[0])


if __name__ == '__main__':
    main2(2250)
