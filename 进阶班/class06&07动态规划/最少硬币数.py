# 【题目】
# 给定数组 arr，arr 中所有的值都为正数。每个值代表一种面值的货币，每种面值
# 的货币可以使用任意张，再给定一个整数 aim，代表要找的钱数，求组成 aim 的最少硬币数。

import random


# 暴力递归
def minCoins1(arr, aim):
    return process1(arr, 0, aim)


def process1(arr, i, rest):
    if rest < 0:
        return -1
    if rest == 0:
        return 0
    if i == len(arr):
        return -1
    yaoi = process1(arr, i + 1, rest - arr[i])
    buyaoi = process1(arr, i + 1, rest)
    if yaoi == -1 and buyaoi == -1:
        return -1
    else:
        if yaoi == -1:
            return buyaoi
        if buyaoi == -1:
            return yaoi + 1
        return min((1 + yaoi), buyaoi)


# 记忆搜索(dp)
def minCoins2(arr, aim):
    dp = [[-2] * (len(arr) + 1) for _ in range(aim + 1)]
    return process2(arr, 0, aim, dp)


def process2(arr, i, rest, dp):
    if rest < 0:
        return -1
    if dp[rest][i] != -2:
        return dp[rest][i]
    if rest == 0:
        dp[rest][i] = 0
    elif i == len(arr):
        dp[rest][i] = -1
    else:
        yaoi = process2(arr, i + 1, rest - arr[i], dp)
        buyaoi = process2(arr, i + 1, rest, dp)
        if yaoi == -1 and buyaoi == -1:
            dp[rest][i] = -1
        elif yaoi == -1:
            dp[rest][i] = buyaoi
        elif buyaoi == -1:
            dp[rest][i] = yaoi + 1
        else:
            dp[rest][i] = min((1 + yaoi), buyaoi)
    return dp[rest][i]


def getRandomArray(l, minsize, maxsize):
    genarray = []
    for i in range(l):
        genarray.append(random.randint(minsize, maxsize))
    return genarray


# 严格表结构(dp)
def minCoins3(arr, aim):
    dp = [[-2] * (len(arr) + 1) for _ in range(aim + 1)]
    for i in range(len(arr), -1, -1):
        for rest in range(0, aim + 1, 1):
            if rest == 0:
                dp[rest][i] = 0
            elif i == len(arr):
                dp[rest][i] = -1
            else:
                yaoi = -1
                buyaoi = dp[rest][i + 1]
                if rest - arr[i] >= 0:
                    yaoi = dp[rest - arr[i]][i + 1]
                if yaoi == -1 and buyaoi == -1:
                    dp[rest][i] = -1
                elif yaoi == -1:
                    dp[rest][i] = buyaoi
                elif buyaoi == -1:
                    dp[rest][i] = yaoi + 1
                else:
                    dp[rest][i] = min((1 + yaoi), buyaoi)
    return dp[aim][0]


if __name__ == "__main__":
    arr = [2, 3, 100]
    aim = 3
    print(minCoins1(arr, aim))
    print(minCoins2(arr, aim))
    print(minCoins3(arr, aim))
    print("-------比较器--------")
    l = 15
    for i in range(10000):
        list = getRandomArray(l, 0, 100)
        if minCoins1(list, 100) != minCoins2(list, 100) \
                or minCoins2(list, 100) != minCoins3(list, 100) \
                or minCoins1(list, 100) != minCoins3(list, 100):
            print("出错！")
            break
    print("成功!")
