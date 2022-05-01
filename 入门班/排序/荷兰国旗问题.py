import random


# 荷兰国旗问题，给定数组和一个数num，将小于等于num的数放左边，大于num的放右边
def Helanguoqiv1(arrs, num):
    if len(arrs) < 2:
        return
    pi = 0
    for i in range(len(arrs)):
        if arrs[i] <= num:
            swap(arrs, i, pi)
            i += 1
            pi += 1
        elif arrs[i] > num:
            i += 1


# 荷兰国旗问题，给定数组和一个数num，将等于num的数放中间，小于num的放左边，大于num的放右边
def Helanguoqiv2(arrs, num):
    if len(arrs) < 2:
        return
    lo = -1
    i = 0
    hi = len(arrs)
    while i<hi:
        if arrs[i] < num:
            lo += 1
            swap(arrs, i, lo)
            i += 1
        elif arrs[i] == num:
            i += 1
        else:
            hi -= 1
            swap(arrs, i, hi)


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
    # Helanguoqiv1(array, 50)
    # print(f"荷兰国旗问题1：{array}")
    Helanguoqiv2(array, 50)
    print(f"荷兰国旗问题2：{array}")
