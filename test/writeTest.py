# Time: 2020/4/25-21:32
# Author: Rex
import pandas as pd
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
def main():

    # df3 = pd.read_excel(r'C:\Users\Administrator\Desktop\initial_excels\df3.xlsx',
    #                     engine='openpyxl', usecols=['卡号'])
    df1 = pd.read_csv(r'C:\Users\Administrator\Desktop\yllCsv\df1.csv', encoding='gbk')
    df2 = pd.read_csv(r'C:\Users\Administrator\Desktop\yllCsv\df2.csv', encoding='gbk')
    # df3 = pd.read_excel(r'C:\Users\Administrator\Desktop\信息.xls')
    # df3 = pd.read_excel(r'C:\Users\Administrator\Desktop\yllTest\df3.xlsx')

    df1.to_csv(r'C:\Users\Administrator\Desktop\yllCsv\df4.csv', mode='w', header=True, index=False)
    df2.to_csv(r'C:\Users\Administrator\Desktop\yllCsv\df4.csv', mode='a', header=False, index=False)



if __name__ == '__main__':
    main()