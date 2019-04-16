# 二分查找，是对有序列表进行操作查找。一般遍历查找的时间复杂度为O(n)，二分查找可以将时间复杂度降低到O(logn)

def binary_search(list, target):
    left, right = 0, len(list)
    if (right == 0):
        return -1
    while (left < right):
        middle = int((left + right) / 2)
        if (list[middle] == target):
            return middle
        elif (list[middle] < target):
            left = middle + 1
        else:
            right = middle - 1
    return -1


if __name__ == '__main__':
    list = [3, 5, 1, 2, 4]
    l = sorted(list)
    # 使用内置函数遍历查找，O(n)
    index1 = l.index(5)
    # 使用二分查找 O(logn)
    index2 = binary_search(l, 5)
    print(index1)
    print(index2)
