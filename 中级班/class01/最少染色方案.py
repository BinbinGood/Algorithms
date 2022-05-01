# 牛牛有一些排成一行的正方形。每个正方形已经被染成红色或者绿色。牛牛现在可
# 以选择任意一个正方形然后用这两种颜色的任意一种进行染色,这个正方形的颜色将
# 会被覆盖。牛牛的目标是在完成染色之后,每个红色R都比每个绿色G距离最左侧近。
# 牛牛想知道他最少需要涂染几个正方形。
# 如样例所示: s = RGRGR
# 我们涂染之后变成RRRGG满足要求了,涂染的个数为2,没有比这个更好的涂染方案
import time


def Minways1(str):
    if len(str) < 1:
        return 0
    mincolor = len(str)
    for i in range(len(str)):
        if i == 0:
            # 统计str中0~len(str)-1位置中R的数量
            mincolor = min(mincolor, getRnum(str, 0, len(str) - 1))
        elif i == len(str) - 1:
            # 统计str中0~len(str)-1位置中G的数量
            mincolor = min(mincolor, (len(str) - getRnum(str, 0, len(str) - 1)))
        else:
            # 统计str中0~i位置中G的数量+str中i+1~len(str)-1位置中R的数量
            mincolor = min(mincolor, (i + 1 - getRnum(str, 0, i)) + getRnum(str, i + 1, len(str) - 1))
    return mincolor


# 统计str中i到j位置中R的数量
def getRnum(str, i, j):
    num = 0
    for index in range(i, j, 1):
        if str[index] == 'R':
            num += 1
    return num


def Minways2(str):
    if len(str) < 1:
        return 0
    mincolor = len(str)
    AB = helpstr(str)
    A, B = AB[0], AB[1]

    for i in range(len(str)):
        if i == 0:
            # 统计str中0~len(str)-1位置中R的数量
            mincolor = min(mincolor, A[len(str)-1])
        elif i == len(str) - 1:
            # 统计str中0~len(str)-1位置中G的数量
            mincolor = min(mincolor, (len(str) - A[len(str)-1]))
        else:
            # 统计str中0~i位置中G的数量+str中i+1~len(str)-1位置中R的数量
            mincolor = min(mincolor, (i + 1 - A[i]) + B[i + 1])
    return mincolor


# 利用辅助数组计算R的数量
# A记录0~i位置上R的数量
# B记录i~n-1位置上R的数量
def helpstr(str):
    A, B = [0] * len(str), [0] * len(str)
    for i in range(len(str)):
        if i == 0 and str[i] == 'R':
            A[i] = 1
            continue
        if str[i] == 'R':
            A[i] = A[i - 1] + 1
        else:
            A[i] = A[i - 1]

    for i in range(len(str) - 1, -1, -1):
        if i == len(str) - 1 and str[i] == 'R':
            B[i] = 1
            continue
        if str[i] == 'R':
            B[i] = B[i + 1] + 1
        else:
            B[i] = B[i + 1]
    return A, B


if __name__ == "__main__":
    str1 = 'RGRGRGRRGGRGGRGRRRGRGRGRGRGGGGGRGRGRGGGGGGGRRRRRRRRRRGG' \
           'GRGRGGGGRRRGGGRRRRRRRRRRGRRRRRRRGGGGRGGGGRGRGRGRRRRRRRGGG' \
           'GGRGRGGGRGRGRGRGRGGGRGRGRGRGRGRGRRRRRGGGRGRGRGGRGRGRGRGRGRG' \
           'RGGGGRRGRGRGRGGR'
    t1 = time.time()
    print(Minways1(str1))
    t2 = time.time()
    print(Minways2(str1))
    t3 = time.time()
    print(f"方法一用时：{(t2 - t1) * 1000}ms,方法二用时{(t3 - t2) * 1000}ms")
