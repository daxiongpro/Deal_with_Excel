import numpy as np

# 聚类结果
type_1 = [7, 8, 9, 11, 19, 25, 32, 35, 36, 38, 46, 55, 61, 65, 73, 75, 80, 88, 95, 96, 98, 100, 105, 107, 112, 114, 116, 117, 118, 119, 121, 122, 125, 129, 135, 140, 141, 147]
type_2 = [1, 2, 5, 12, 14, 16, 17, 18, 20, 21, 22, 24, 26, 30, 31, 33, 37, 39, 41, 43, 45, 48, 52, 56, 58, 63, 64, 66, 67, 68, 70, 76, 79, 82, 83, 84, 87, 89, 91, 92, 93, 94, 97, 102, 103, 106, 108, 123, 126, 127, 130, 131, 132, 136, 137, 139, 142, 144, 145, 146, 148, 149]
type_3 = [0, 3, 4, 6, 10, 13, 15, 23, 27, 28, 29, 34, 40, 42, 44, 47, 49, 50, 51, 53, 54, 57, 59, 60, 62, 69, 71, 72, 74, 77, 78, 81, 85, 86, 90, 99, 101, 104, 109, 110, 111, 113, 115, 120, 124, 128, 133, 134, 138, 143]
# ground_truth结果
type_one = [0, 3, 4, 6, 10, 13, 15, 23, 27, 28, 29, 34, 40, 42, 44, 47, 49, 50, 51, 53, 54, 57, 59, 60, 62, 69, 71, 72, 74, 77, 78, 81, 85, 86, 90, 99, 101, 104, 109, 110, 111, 113, 115, 120, 124, 128, 133, 134, 138, 143]
type_two = [5, 7, 16, 17, 18, 20, 21, 22, 24, 26, 31, 33, 37, 39, 43, 45, 48, 56, 58, 63, 64, 66, 67, 68, 70, 76, 79, 82, 83, 87, 89, 92, 93, 94, 97, 102, 103, 106, 119, 123, 126, 130, 131, 132, 136, 137, 142, 144, 148, 149]
type_three = [1, 2, 8, 9, 11, 12, 14, 19, 25, 30, 32, 35, 36, 38, 41, 46, 52, 55, 61, 65, 73, 75, 80, 84, 88, 91, 95, 96, 98, 100, 105, 107, 108, 112, 114, 116, 117, 118, 121, 122, 125, 127, 129, 135, 139, 140, 141, 145, 146, 147]
# 进行结果比较
# 找到重复元素（交集）
def find_same(list1,list_one):
    inters = np.intersect1d(list1, list_one)
    # 元素个数索引转换
    bc1 = np.bincount(list1)
    bc2 = np.bincount(list_one)
    # 统计相同元素匹配个数
    same_count_list = [min(bc1[x], bc2[x]) for x in inters]
    same_count = sum(same_count_list)/max(len(list1),len(list_one))
    print(same_count)
    return same_count

# 计算精确度

acc1 = find_same(type_1,type_three)
acc2 = find_same(type_one,type_3)
acc3 = find_same(type_2,type_two)
acc = (acc1 + acc2 + acc3)/3
print(acc)