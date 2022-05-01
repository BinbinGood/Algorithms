import random


# 选择排序
def SelectionSort(arr):
    if len(arr) < 2:
        return
    l = len(arr)
    for i in range(l):
        temp = i
        for j in range(i + 1, l):
            if arr[temp] > arr[j]:
                temp = j
        swap(arr, temp, i)


# 冒泡排序
def BubbleSort(arr):
    if len(arr) < 2:
        return
    for i in range(len(arr)):
        for j in range(len(arr) - (i + 1)):
            if arr[j] > arr[j + 1]:
                swap(arr, j, j + 1)


# 插入排序
def InsertSort(arr):
    for i in range(len(arr)):
        for j in range(i, 0, -1):
            if arr[j] < arr[j - 1]:
                swap(arr, j, j - 1)


# 交换函数
def swap(arr, temp, i):
    tem = arr[temp]
    arr[temp] = arr[i]
    arr[i] = tem


# 此函数将产生一个长度为L的数组，数组元素大小在minsize到maxsize范围内
def generateArray(l, minsize, maxsize):
    genarray = []
    for i in range(l):
        genarray.append(random.randint(minsize, maxsize))
    return genarray


if __name__ == "__main__":
    array = generateArray(20, 0, 100)
    array1 = array[:]
    print(array)
    SelectionSort(array)
    print(array)
    # BubbleSort(array1)
    # print(array1)
    InsertSort(array1)
    print(array1)
