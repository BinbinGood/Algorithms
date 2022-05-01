# 给定一个非负整数n，代表二叉树的节点个数。返回能形成多少种不同的二叉树结构
import random


def treenum1(n):
    if n < 0:
        return
    return process(n)


def process(n):
    if n == 0 or n == 1:
        return 1
    res = 0
    for left in range(n):
        res += process(left) * process(n - 1 - left)
    return res


# 动态规划
def treenum2(n):
    if n < 0:
        return
    if n == 0 or n == 1:
        return 1
    dp = [0] * (n + 1)
    dp[0] = dp[1] = 1
    for nodes in range(2, n + 1, 1):
        for left in range(nodes):
            dp[nodes] += dp[left] * dp[nodes - 1 - left]
    return dp[n]


if __name__ == "__main__":
    n = 15
    print(treenum1(n))
    print(treenum2(n))
    print("-----------")
    # for i in range(11):
    #     if treenum1(i) != treenum2(i):
    #         print("出错")
    #         break
