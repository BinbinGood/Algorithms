import random


def RadixSort(arr):
    if len(arr) < 2:
        return
    sort(arr, 0, len(arr) - 1, maxbits(arr))


# 获取最大值的位数
def maxbits(arr):
    maxnum = 0
    for i in range(len(arr)):
        if arr[i] > maxnum:
            maxnum = arr[i]
    res = 0
    while maxnum != 0:
        res += 1
        maxnum = maxnum // 10  # 向下取整
    return res


def sort(arr, lo, hi, digit):
    radix = 10
    bucket = [0] * (hi - lo + 1)  # 辅助空间
    for d in range(1, digit + 1):  # 进行多少次入桶出桶
        count = [0 for v in range(radix)]
        # 统计第d位各个数字的词频
        for i in range(lo, hi + 1):
            j = getDigit(arr[i], d)
            count[j] += 1
        # count数组中比第i个数字小于等于的数的个数（前缀和数组）
        for i in range(1, radix):
            count[i] = count[i] + count[i - 1]
        # 从右往左将数放入辅助数组中
        for i in range(hi, lo - 1, -1): # 注意范围!!!!
            j = getDigit(arr[i], d)
            bucket[count[j] - 1] = arr[i]
            count[j] -= 1
        # 将辅助数组中的数复制回原数组
        i = lo
        j = 0
        while i <= hi:
            arr[i] = bucket[j]
            i += 1
            j += 1


# 获取数字num第d位的值
def getDigit(num, d):
    return (num // int(10 ** (d - 1))) % 10


# 此函数将产生一个长度为L的数组，数组元素大小在minsize到maxsize范围内
def generateArray(l, minsize, maxsize):
    genarray = []
    for i in range(l):
        genarray.append(random.randint(minsize, maxsize))
    return genarray


if __name__ == "__main__":
    times = 10000
    succedflag = True
    for time in range(times):
        array = generateArray(50, 0, 100)
        array1 = array[:]
        RadixSort(array)
        array1.sort()
        if array1 != array:
            print("出错")
            succedflag = False
            print(array1)
            print(array)
            break
    if succedflag:
        print("成功")