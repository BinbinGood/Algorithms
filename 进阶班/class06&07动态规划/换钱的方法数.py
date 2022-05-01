# 给定数组 arr，arr 中所有的值都为正数且不重复。每个值代表一种面值的货币，每种面值
# 的货币可以使用任意张，再给定一个整数 aim，代表要找的钱数，求组成 aim 的方法数
import random


def process(arr, i, rest):
    if i == len(arr):
        return 1 if rest == 0 else 0
    ways, zhang = 0, 0
    while arr[i] * zhang <= rest:
        ways += process(arr, i + 1, rest - arr[i] * zhang)
        zhang += 1
    return ways


def getways1(arr, aim):
    if aim <= 0:
        return 0
    return process(arr, 0, aim)


def getways2(arr, aim):
    if aim <= 0:
        return 0
    dp = [[0] * (aim + 1) for _ in range(len(arr) + 1)]
    dp[len(arr)][0] = 1
    for i in range(len(arr) - 1, -1, -1):
        for rest in range(aim + 1):
            ways, zhang = 0, 0
            while arr[i] * zhang <= rest:
                ways += dp[i + 1][rest - arr[i] * zhang]
                zhang += 1
            dp[i][rest] = ways
    return dp[0][aim]


def getways3(arr, aim):
    if aim <= 0:
        return 0
    dp = [[0] * (aim + 1) for _ in range(len(arr) + 1)]
    dp[len(arr)][0] = 1
    for i in range(len(arr) - 1, -1, -1):
        for rest in range(aim + 1):
            dp[i][rest] = dp[i + 1][rest]
            if rest - arr[i] >= 0:
                dp[i][rest] += dp[i][rest - arr[i]]
    return dp[0][aim]


# 不重复生成数字
def getRandomArray(l, minsize, maxsize):
    return random.sample(range(minsize, maxsize), l)


if __name__ == "__main__":
    str1 = [3, 5, 20, 100, 50, 5, 7, 2, 1, 9, 10, 70]
    aim = 3
    print(getways1(str1, aim))
    print(getways2(str1, aim))
    print(getways3(str1, aim))
    print("-------比较器--------")
    for index in range(1000):
        list = getRandomArray(10, 1, 100)
        result1 = getways1(list, 100)
        result2 = getways2(list, 100)
        result3 = getways3(list, 100)
        if result1 != result2 or result2 != result3:
            print("出错！")
            break
    print("成功!")
