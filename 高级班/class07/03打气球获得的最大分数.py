# KMP算法扩展题目二
# 给定一个数组 arr，代表一排有分数的气球。每打爆一个气球都能获得分数，假设打爆气
# 球 的分数为 X，获得分数的规则如下:
# 1)如果被打爆气球的左边有没被打爆的气球，找到离被打爆气球最近的气球，假设分数为
# L;如果被打爆气球的右边有没被打爆的气球，找到离被打爆气球最近的气球，假设分数为
# R。 获得分数为 L*X*R。
# 2)如果被打爆气球的左边有没被打爆的气球，找到离被打爆气球最近的气球，假设分数为
# L;如果被打爆气球的右边所有气球都已经被打爆。获得分数为 L*X。
# 3)如果被打爆气球的左边所有的气球都已经被打爆;如果被打爆气球的右边有没被打爆的
# 气球，找到离被打爆气球最近的气球，假设分数为 R;获得分数为 X*R。
# 4)如果被打爆气球的左边和右边所有的气球都已经被打爆。获得分数为 X。
# 目标是打爆所有气球，获得每次打爆的分数。通过选择打爆气球的顺序，可以得到不同
# 的
# 总分，请返回能获得的最大分数。
# 【举例】
# arr = {3,2,5}
# 如果先打爆3，获得3*2；再打爆2，获得2*5；最后打爆5，获得5；最后总分21
# 如果先打爆3，获得3*2;再打爆5，获得2*5；最后打爆2，获得2；最后总分18
# 如果先打爆2，获得3*2*5；再打爆3，获得3*5；最后打爆5，获得5；最后总分50
# 如果先打爆2，获得3*2*5；再打爆5，获得3*5；最后打爆3，获得3；最后总分48
# 如果先打爆5，获得2*5；再打爆3，获得3*2；最后打爆2，获得2；最后总分18
# 如果先打爆5，获得2*5;再打爆2，获得3*2；最后打爆3，获得3；最后总分19
# 返回能获得的最大分数为50


def maxCoins1(arr):
    if len(arr) == 0:
        return 0
    help = [0] * (len(arr) + 2)
    help[0] = 1
    help[-1] = 1
    for i in range(len(arr)):
        help[i + 1] = arr[i]
    return process(help, 1, len(arr))


# 打爆L到R范围上所有的气球，返回最大的分数
# 假设L-1和R+1一定没有被打爆
# 尝试方式：每个位置的气球都最后打爆
def process(arr, L, R):
    if L == R:
        return arr[L - 1] * arr[L] * arr[R + 1]
    # 最后打爆arr[L]的方案，和最后打爆arr[R]的方案，先比较一下
    maxres = max(arr[L - 1] * arr[L] * arr[R + 1] + process(arr, L + 1, R),
                 arr[L - 1] * arr[R] * arr[R + 1] + process(arr, L, R - 1))
    # 尝试中间位置的气球最后被打爆的每一种方案
    for i in range(L + 1, R):
        maxres = max(maxres,
                     arr[L - 1] * arr[i] * arr[R + 1] +
                     process(arr, L, i - 1) + process(arr, i + 1, R))
    return maxres


def maxCoins2(help):
    if len(help) == 0:
        return 0
    help = [0] * (len(arr) + 2)
    help[0] = 1
    help[-1] = 1
    for i in range(len(arr)):
        help[i + 1] = arr[i]
    # 动态表
    dp = [[0] * (len(arr) + 1) for _ in range(len(arr) + 1)]
    # 对角线
    for k in range(len(dp)):
        dp[k][k] = help[k - 1] * help[k] * help[k + 1]

    for L in range(len(dp) - 1, 0, -1):
        for R in range(L + 1, len(dp[0])):
            maxres = max(help[L - 1] * help[L] * help[R + 1] + dp[L + 1][R],
                         help[L - 1] * help[R] * help[R + 1] + dp[L][R - 1])
            # 尝试中间位置的气球最后被打爆的每一种方案
            for i in range(L + 1, R):
                maxres = max(maxres,
                             help[L - 1] * help[i] * help[R + 1] +
                             dp[L][i - 1] + dp[i + 1][R])
            dp[L][R] = maxres
    return dp[1][len(arr)]


arr = [3, 2, 5, 10, 5, 4, 6, 20, 51, 63, 70]
print(maxCoins1(arr))
print(maxCoins2(arr))
