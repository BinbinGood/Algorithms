import random


# 归并排序
def MergeSort(arr):
    if len(arr) < 2:
        return
    lo = 0
    hi = len(arr) - 1
    sort(arr, lo, hi)


def sort(arr, lo, hi):
    if lo == hi:
        return
    mid = int(lo + (hi - lo) / 2)
    sort(arr, lo, mid)
    sort(arr, mid + 1, hi)
    merge(arr, lo, mid, hi)  # 归并排序先分，直到不可分割以后调用归并函数。将两个排好序的数组合并到一起


def merge(arr, lo, mid, hi):
    p1 = lo
    p2 = mid + 1
    help = []
    while p1 <= mid and p2 <= hi:  # 不能用&！！！
        # 从左到右走一遍，谁小就把谁先放入辅助数组中
        if arr[p1] <= arr[p2]:
            help.append(arr[p1])
            p1 += 1
        else:
            help.append(arr[p2])
            p2 += 1
    # 将剩余的数放入辅助数组中
    while p1 <= mid:
        help.append(arr[p1])
        p1 += 1
    while p2 <= hi:
        help.append(arr[p2])
        p2 += 1
    # 依次将辅助数组中的数放入原始数组中
    for i in range(len(help)):
        arr[lo + i] = help[i]


# 此函数将产生一个长度为L的数组，数组元素大小在minsize到maxsize范围内
def generateArray(l, minsize, maxsize):
    genarray = []
    for i in range(l):
        genarray.append(random.randint(minsize, maxsize))
    return genarray


if __name__ == "__main__":
    array = generateArray(20, 0, 100)
    print(array)
    MergeSort(array)
    print(array)
