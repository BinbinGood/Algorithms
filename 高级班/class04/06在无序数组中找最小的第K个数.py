# 在一个无序数组中，求最小的第k个数。

# K>0
def getMinKthByBFPRT(arr, k):
    if len(arr) == 0:
        return 0
    return select(arr, 0, len(arr) - 1, k - 1)


# 在arr[begin~end]范围上，求如果排序的话，i位置的数是谁，返回
# i一定在begin~end范围上
def select(arr, begin, end, i):
    if begin == end:
        return arr[begin]
    privot = medianOfMedians(arr, begin, end)
    privotrange = partition(arr, begin, end, privot)
    if privotrange[0] <= i <= privotrange[1]:
        return arr[i]
    elif privotrange[0] > i:
        return select(arr, begin, privotrange[0] - 1, i)
    else:
        return select(arr, privotrange[1] + 1, end, i)


# 从begin到end分组选出中位数，组成数组marr，从中间选出中位数
def medianOfMedians(arr, begin, end):
    num = end - begin + 1  # 数的个数
    offset = 0 if num % 5 == 0 else 1
    marr = [0] * (num // 5 + offset)
    for i in range(len(marr)):
        begini = begin + i * 5
        endi = begini + 4
        marr[i] = getmedian(arr, begini, min(endi, end))
    return select(marr, 0, len(marr) - 1, len(marr) // 2)


# 荷兰国旗问题，返回等于区域的上下界
def partition(arr, begin, end, priot):
    small = begin - 1
    big = end + 1
    cur = begin
    while cur < big:
        if arr[cur] < priot:
            small += 1
            swap(arr, cur, small)
            cur += 1
        elif arr[cur] == priot:
            cur += 1
        else:
            big -= 1
            swap(arr, cur, big)
    return [small + 1, big - 1]  # 返回等于区域的上下界坐标


# 获取arr中begin到end的中位数
def getmedian(arr, begin, end):
    insertionsort(arr, begin, end)
    sum = begin + end
    mid = (sum // 2) + sum % 2  # 上中位数
    return arr[mid]


# 利用插入排序，将数组从begin到end的数据，进行排序
def insertionsort(arr, begin, end):
    for i in range(begin + 1, end + 1, 1):
        for j in range(i, begin, -1):
            if arr[j - 1] > arr[j]:
                swap(arr, j - 1, j)
            else:
                break


# 数组i和j位置交换
def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp


arr = [3, 4, 5, 7, 1, 9, 2, 10]
print(getMinKthByBFPRT(arr, 2))
