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

import utils

first = True


class Deal():
    def __init__(self):
        subway_csv = 'static/csvFiles/df3.csv'
        bus_all_csv = 'static/csvFiles/df4.csv'
        self.result_path = 'static/csvFiles/result.csv'
        # 将csv转换成pandas的dataframe格式
        self.subway_df = pd.read_csv(subway_csv, encoding='gbk')
        self.bus_all_df = pd.read_csv(bus_all_csv)

        self.bus_dict_ = utils.list_to_dict(self.bus_all_df.iloc[:, 0])  # 比较耗时

    def run(self):
        for index, subway_row in self.subway_df.iterrows():
            card_id = subway_row[0]
            indexes = utils.find_indexes(self.bus_dict_, card_id)  # 从bus_all.csv中找card_id，返回index列表，没找到返回空列表
            if len(indexes) != 0:  # 在bus_all_csv中找到了
                subway_time = datetime.strptime(subway_row[3], "%H:%M:%S")  # 地铁出站时间
                # 找出在df4中位置为indexes_in_df4的时间与t1最近的那行的index,没找到返回None
                closest_index = utils.find_closest_time(self.bus_all_df, indexes, subway_time)
                if closest_index is not None:
                    bus_row = self.bus_all_df.iloc[closest_index, :]
                    utils.save(self.result_path, subway_row, bus_row)
                    print('第', index, '行写入成功！')
                else:
                    print('卡号：', subway_row[0], '公交上车时间都在地铁时间之前')
            else:
                print('没找到第', index, '行的id', subway_row[0])


if __name__ == '__main__':
    deal = Deal()
    deal.run()
