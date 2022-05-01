import random


def QuickSort(arr):
    if len(arr) < 2:
        return
    lo = 0
    hi = len(arr) - 1
    sort(arr, lo, hi)


def sort(arr, lo, hi):
    if lo >= hi:
        return
    p = partition(arr, lo, hi)
    sort(arr, lo, p[0] - 1)  # 递归调用，分别在左边和右边进行快速排序
    sort(arr, p[1] + 1, hi)


# 该函数实现arr数组从lo到hi的位置进行划分为左侧小于arr[hi]右侧大于arr[hi]等于arr[hi]的数放中间，
# 最终返回arr数组中间等于arr[hi]的数的下标范围，
def partition(arr, lo, hi):
    p1 = lo - 1
    p2 = hi  # 最右边存放的是这个部分用来划分的数
    i = lo
    while i < p2:
        if arr[i] < arr[hi]:
            p1 += 1
            swap(arr, i, p1)
            i += 1
        elif arr[i] > arr[hi]:
            p2 -= 1
            swap(arr, i, p2)
        else:
            i += 1
    swap(arr, p2, hi)  # 最后将这个没有参与排序的数放到中间
    return [p1 + 1, p2] # 小于区域的下一个元素就是等于的首位置，p2此时就在等于区域的最后一个位置


# 将arrs数组中a、b索引位置的数进行交换
def swap(arrs, a, b):
    temp = arrs[a]
    arrs[a] = arrs[b]
    arrs[b] = temp


# 此函数将产生一个长度为L的数组，数组元素大小在minsize到maxsize范围内
def generateArray(l, minsize, maxsize):
    genarray = []
    for i in range(l):
        genarray.append(random.randint(minsize, maxsize))
    return genarray


if __name__ == "__main__":
    array = generateArray(20, 0, 100)
    print(array)
    QuickSort(array)
    print(array)
