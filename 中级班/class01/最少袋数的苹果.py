# 小虎去附近的商店买苹果，奸诈的商贩使用了捆绑交易，只提供6个每袋和8个
# 每袋的包装包装不可拆分。可是小虎现在只想购买恰好n个苹果，小虎想购买尽
# 量少的袋数方便携带。如果不能购买恰好n个苹果，小虎将不会购买。输入一个
# 整数n，表示小虎想购买的个苹果，返回最小使用多少袋子。如果无论如何都不
# 能正好装下，返回-1。
import random
import time


# 递归方法
def Minbags1(N):
    if N < 6:
        return -1
    return process(N, 0, N)


def process(N, i, rest):
    if i > int(N / 6) or rest < 0:
        return -1
    if rest == 0:
        return 0
    six = process(N, i + 1, rest - 6)
    eight = process(N, i + 1, rest - 8)
    if six == -1 and eight == -1:
        return -1
    elif six == -1:
        return eight + 1
    elif eight == -1:
        return six + 1
    else:
        return 1 + min(six, eight)


# 利用递归改的动态规划版本
def Minbags2(N):
    if N < 6:
        return -1
    dp = [[-1] * (N + 1) for _ in range(int(N / 6) + 1)]
    for i in range(int(N / 6), -1, -1):
        for rest in range(N + 1):
            if rest == 0:
                dp[i][rest] = 0
                continue
            six = getvalue(dp, N, i + 1, rest - 6)
            eight = getvalue(dp, N, i + 1, rest - 8)
            if six == -1 and eight == -1:
                dp[i][rest] = -1
            elif six == -1:
                dp[i][rest] = eight + 1
            elif eight == -1:
                dp[i][rest] = six + 1
            else:
                dp[i][rest] = 1 + min(six, eight)
    return dp[0][N]


def getvalue(dp, N, i, rest):
    if i > int(N / 6) or rest < 0:
        return -1
    return dp[i][rest]


# 方法三 利用贪心策略，使用尽可能多的能装8个苹果的袋子
def Minbags3(N):
    eight = int(N / 8)
    six = -1
    rest = N - 8 * eight
    while rest < 24 and eight >= 0:
        restuse6 = minuse6(rest)
        if restuse6 != -1:
            six = restuse6
            break
        eight -= 1
        rest = N - 8 * eight
    return -1 if six == -1 else eight + six


def minuse6(rest):
    return int(rest / 6) if rest % 6 == 0 else -1


# 方法四 根据输入输出的规律直接得到的
def Minbags4(N):
    if N & 1 != 0:  # 奇数
        return -1
    if N >= 18:
        return int((N - 18) / 8) + 3
    elif N == 0:
        return 0
    elif N == 6 or N == 8:
        return 1
    elif N == 12 or N == 14 or N == 18:
        return 2
    else:
        return -1


if __name__ == "__main__":
    N = 100000
    t1 = time.time()
    # print(Minbags1(N))
    t2 = time.time()
    print(f"方法一费时：{(t2 - t1) * 1000}ms")
    # print(Minbags2(N))
    t3 = time.time()
    print(f"方法二费时：{(t3 - t2) * 1000}ms")
    print(Minbags3(N))
    t4 = time.time()
    print(f"方法三费时：{(t4 - t3) * 1000}ms")
    # print("------找输入输出的规律-------")
    # for i in range(50):
    #     print(f"当N等于{i}时的输出为：{Minbags3(i)}")
    # print("---------------------------")
    t5 = time.time()
    print(Minbags4(N))
    t6 = time.time()
    print(f"方法四费时：{(t6 - t5) * 1000}ms")
