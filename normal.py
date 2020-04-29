# Time: 2020/4/25-21:32
# Author: Rex
from datetime import datetime

import pandas as pd

file1 = r'C:\Users\Administrator\Desktop\yllCsv\df1.csv'
file2 = r'C:\Users\Administrator\Desktop\yllCsv\df2.csv'
file3 = r'C:\Users\Administrator\Desktop\yllCsv\df3.csv'
df1 = pd.read_csv(file1, encoding='gbk')
df2 = pd.read_csv(file2, encoding='gbk')
df3 = pd.read_csv(file3, encoding='gbk')


def find_id_in_bus(file, line):
    '''
    pd3中的line行第0列的数据与file(pd1或 pd2)中的line第0列比对
    取file中时间在pd3之后的时间差最小数据
    返回file中的line
    没找到返回None
    '''

    if file == file1:
        df = df1
    elif file == file2:
        df = df2
    else:
        print('没有file')

    nrows = df.shape[0]
    row_list = []
    for i in range(nrows):
        row = df.iloc[i]
        if row[0] == line[0]:
            t1 = datetime.strptime(str(row[3]), "%H:%M:%S")
            t2 = datetime.strptime(str(line[3]), "%H:%M:%S")
            if t2 > t1:
                row_list.append(row)
    if len(row_list):
        nowsub = datetime.strptime(row_list[0][3], "%H:%M:%S") - datetime.strptime(line[3], "%H:%M:%S")
        nowitem = row_list[0]
        for item in row_list:
            if datetime.strptime(item[3], "%H:%M:%S") - datetime.strptime(line[3], "%H:%M:%S") < nowsub:
                nowsub = datetime.strptime(item[3], "%H:%M:%S") - datetime.strptime(line[3], "%H:%M:%S")
                nowitem = item
        return nowitem

    else:
        return None


def main():
    # 获取最大行，最大列
    nrows3 = df3.shape[0]
    for i in range(nrows3):
        row = df3.iloc[i]
        data_list = []
        try:
            data1 = find_id_in_bus(file1, row)
            data2 = find_id_in_bus(file2, row)
            # print(type(data1) == pd.core.series.Series)
            # print(type(data2) == pd.core.series.Series)
            if type(data1) == pd.core.series.Series and type(data2) == pd.core.series.Series:
                if data1[3] > data2[3]:
                    data = data1
                else:
                    data = data2
            elif type(data1) == pd.core.series.Series:
                data = data1
            elif type(data2) == pd.core.series.Series:
                data = data2
            else:
                data = None
                print('没找到第', i + 2, '行的id', str(row[0]), end='\n')

            if type(data) == pd.core.series.Series:
                print('卡号：', row[0],
                      '地铁下车时间：', row[3],
                      '公交上车时间：', data[3], end='\n')
        except Exception as e:
            print('发生错误:', e)



if __name__ == '__main__':
    main()
