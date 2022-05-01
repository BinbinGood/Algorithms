# 给定两个字符串str1和str2，再给定三个整数ic、dc和rc，分别代表插入、删
# 除和替换一个字符的代价，返回将str1编辑成str2的最小代价。
# 【举例】
# str1="abc"，str2="adc"，ic=5，dc=3，rc=2
# 从"abc"编辑成"adc"，把'b'替换成'd'是代价最小的，所以返回2
# str1="abc"，str2="adc"，ic=5，dc=3，rc=100
# 从"abc"编辑成"adc"，先删除'b'，然后插入'd'是代价最小的，所以返回8
# str1="abc"，str2="abc"，ic=5，dc=3，rc=2
# 不用编辑了，本来就是一样的字符串，所以返回0

def minCost(str1, str2, ic, dc, rc):
    dp = [[0] * (len(str2) + 1) for _ in range(len(str1) + 1)]
    for i in range(len(dp)):
        dp[i][0] = dc * i
    for j in range(len(dp[0])):
        dp[0][j] = ic * j

    for i in range(1, len(dp)):
        for j in range(1, len(dp[0])):
            dp[i][j] = dp[i - 1][j - 1]
            if str1[i - 1] != str2[j - 1]:
                dp[i][j] += rc
            dp[i][j] = min(dp[i - 1][j] + ic, min(dp[i][j], dp[i][j - 1] + dc))
    return dp[len(str1)][len(str2)]


str1 = 'abc'
str2 = 'adc'
print(minCost(str1, str2, 5, 3, 2))
