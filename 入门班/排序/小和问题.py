import random


# 小和问题就是在归并排序的基础上改造的
# 此方法使得时间复杂度为：O(nlogn)
# 在一个数组中，每一个数左边比当前数小的数累加起来，叫做这个数组
# 的小和。求一个数组 的小和。
# 例子:[1,3,4,2,5] 1左边比1小的数，没有; 3左边比3小的数，1; 4左
# 边比4小的数，1、3; 2左边比2小的数，1; 5左边比5小的数，1、3、4、
# 2; 所以小和为1+1+3+1+1+3+4+2=16
# 归并排序
def MergeSort(arr):
    if len(arr) < 2:
        return
    lo = 0
    hi = len(arr) - 1
    return sort(arr, lo, hi)


def sort(arr, lo, hi):
    if lo == hi:
        return 0
    mid = int(lo + (hi - lo) / 2)
    return sort(arr, lo, mid) + sort(arr, mid + 1, hi) + merge(arr, lo, mid, hi)


def merge(arr, lo, mid, hi):
    p1 = lo
    p2 = mid + 1
    help = []
    res = 0
    while p1 <= mid and p2 <= hi:  # 不能用&！！！
        if arr[p1] < arr[p2]:
            help.append(arr[p1])
            res += (hi - p2 + 1) * arr[p1]
            p1 += 1
        else:
            help.append(arr[p2])
            p2 += 1
    while p1 <= mid:
        help.append(arr[p1])
        p1 += 1
    while p2 <= hi:
        help.append(arr[p2])
        p2 += 1
    for i in range(len(help)):
        arr[lo + i] = help[i]

    return res


# 定义一个比较器，测试算法的正确性
def Comparator(arr):
    if len(arr) < 2:
        return
    res = 0
    for i in range(len(arr)):
        for j in range(i):
            if arr[i] > arr[j]:
                res += arr[j]
    return res


# 此函数将产生一个长度为L的数组，数组元素大小在minsize到maxsize范围内
def generateArray(l, minsize, maxsize):
    genarray = []
    for i in range(l):
        genarray.append(random.randint(minsize, maxsize))
    return genarray


if __name__ == "__main__":
    times = 1
    succedflag = True
    for time in range(times):
        array = generateArray(20, 0, 100)
        # array = [1,3,4,2,5]
        array1 = array[:]
        if MergeSort(array1) != Comparator(array):
            print("出错")
            succedflag = False
            print(array1)
            print(array)
            break
    if succedflag:
        print("成功")
