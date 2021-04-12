# Time: 2020/4/27-9:53
# Author: Rex
# Time: 2020/4/26-15:06
# Author: Rex
# Time: 2020/4/26-11:44
# Author: Rex

"""
df1是11点之前
df2是11点之后
df3是要查询的对应文件
df4是将df1和df2拼起来的文件
处理时直接处理df4
df5是输出保存的excel
"""
from datetime import datetime

import pandas as pd

first = True


class Deal():
    def __init__(self):
        file1 = 'static/csvFiles/bus1_df.csv'
        file2 = 'static/csvFiles/bus2_df.csv'
        file3 = 'static/csvFiles/subway_df.csv'
        file4 = 'static/csvFiles/bus_all_df.csv'
        result = 'static/csvFiles/result.csv'

        self.bus1_df = pd.read_csv(file1, encoding='gbk')
        self.bus2_df = pd.read_csv(file2, encoding='gbk')
        self.subway_df = pd.read_csv(file3, encoding='gbk')
        self.bus_all_df = pd.read_csv(file4)
        self.result_csv_df = pd.read_csv(result)

        self.bus_dic = self._list_to_dict(self.bus_all_df.iloc[:, 0])
        # self.dic_in_df5 = self._list_to_dict(self.result_csv_df.iloc[:, 0])

    def run(self):
        for index, row in self.subway_df.iterrows():
            card_id = row[0]
            # 从df4中找idCard，返回index列表，没找到返回空列表
            indexes_df4 = self._find_indexes(card_id)
            # 在df4中找到了
            if len(indexes_df4) != 0:

                subway_time = datetime.strptime(row[3], "%H:%M:%S")  # 地铁出站时间
                # 找出在df4中位置为indexes_in_df4的时间与t1最近的那行的index,没找到返回None
                close_index = self._find_closest_time(self.bus_all_df, indexes_df4, subway_time)
                if close_index != None:
                    self._save(self.result, row, self.bus_all_df.iloc[close_index, :])
                    print('第', index, '行写入成功！')
                else:
                    print('卡号：', row[0], '公交上车时间都在地铁时间之前')
            else:
                print('没找到第', index, '行的id', row[0])

    def _list_to_dict(self, list_):
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

    def _find_indexes(self, card_id):
        # 从df4中找idCard，返回index列表，没找到返回空列表
        # 先建立哈希表

        if card_id in self.bus_dic.keys():
            return self.bus_dic[card_id]
        else:
            return []

    def _find_closest_time(self, df, indexes_in_df4, time):
        # 在df中找到与time最接近的时间，并返回这一行的index
        flag = False  # 是否找到过一个

        now_index = None
        for index in indexes_in_df4:
            row = df.iloc[index, :]
            # 第一次找到之前比较只需看是否在地铁时间之后
            if flag == False:
                if time < datetime.strptime(row[3], "%H:%M:%S"):
                    now_close_time = datetime.strptime(row[3], "%H:%M:%S")
                    now_index = index
                    flag = True
            # 第二次之后的比较，需要与
            else:
                if time < datetime.strptime(row[3], "%H:%M:%S") < now_close_time:
                    now_close_time = datetime.strptime(row[3], "%H:%M:%S")
                    now_index = index

        return now_index

    def _save(self, file, row_subway, row_bus):
        """
        :param file: 保存到的文件地址
        :param row_subway: 地铁下车的行信息
        :param row_bus: 公交上车的行信息
        :return:
        """
        global first
        dic = {
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
        df = pd.DataFrame(dic)

        if first == True:
            df.to_csv(file, mode='w', header=True, index=False)
            first = False
        else:
            df.to_csv(file, mode='a', header=False, index=False)


class OtherCode():

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
        # global result_csv_df
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
    # print(dic_in_df5)
    # print(len(result_csv_df))
    # print(result_csv_df.iloc[27578, :])
    main2()
