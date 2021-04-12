# Time: 2020/4/26-11:27
# Author: Rex
import collections

ls = ['a', 'b', 'c', 'a']
# dic = {
#     'a': 1,
#     'b': 2,
#     'c': 3,
#     'a': 4
# }



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

dic = list_to_dict(ls)
print('e' in dic.keys())
print(list_to_dict(ls))
