# 给定一个字符串str，返回把str全部切成回文子串的最小分割数。
# 【举例】
# str="ABA"。
# 不需要切割，str本身就是回文串，所以返回0。
# str="ACDCDCDAD"。
# 最少需要切2次变成3个回文子串，比如"A"、"CDCDC"和"DAD"，所以返回2。

# 该函数判断str[i-j]是否为回文结构，返回一个dp数组
def vaild(str1):
    dp = [[False] * len(str1) for _ in range(len(str1))]
    # 对角线
    for k in range(len(str1)):
        dp[k][k] = True
    i, j = 0, 1
    while i < len(str1) - 1:
        if str1[i] == str1[j]:
            dp[i][j] = True
        i += 1
        j += 1
    for i in range(len(str1) - 3, -1, -1):
        for j in range(i + 2, len(str1)):
            if str1[i] == str1[j]:
                dp[i][j] = dp[i + 1][j - 1]
    return dp


def Minsplitnum(str1):
    if len(str1) <= 1:
        return 0
    vailddp = vaild(str1)
    dp = [0] * (len(str1) + 1)
    dp[len(str1)] = -1  # 为了将最后一个过程加的1抵消掉
    for i in range(len(str1) - 1, -1, -1):
        dp[i] = len(str1) - 1  # 假设一个最大值
        for end in range(i, len(str1)):
            if vailddp[i][end]:
                dp[i] = min(dp[i], 1 + dp[end + 1])
    return dp[0]


str1 = "ACDCDCDAD"
print(Minsplitnum(str1))
