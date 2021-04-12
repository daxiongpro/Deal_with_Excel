# Time: 2020/7/1-14:35
# Author: Rex
import pandas as pd

file1 = r'D:\宁大\数据结构助教\学生成绩汇总.xlsx'
file2 = r'C:\Users\Administrator\Desktop\数据结构与算法-实验课成绩_project成绩.xls'

df1 = pd.read_excel(file1)
df2 = pd.read_excel(file2)
# print(bus2)
cols = df2.iloc[4:, 10]
# cols = bus1.iloc[:, 4]
print(cols)