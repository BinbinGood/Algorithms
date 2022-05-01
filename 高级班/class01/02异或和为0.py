# 给出n个数字 a_1,...,a_n，问最多有多少不重叠的非空区间，使得每个区间内数字的
# xor都等于0。

def mostEOR(arr):
    xor = 0
    dp = [0] * len(arr)  # 保存0~i最后划分的情况下，异或和为0最多的部分是多少个
    map = dict()  # 哈希表，从0出发的前缀异或和，前缀异或和对应的出现的最晚位置
    map[0] = -1
    for i in range(len(arr)):  # i所在的最后一块
        xor ^= arr[i]  # 前缀异或和
        if xor in map:  # if中了表示有第二种可能性
            pre = map[xor]  # pre+1~i是最后划分的最后一个部分
            dp[i] = 1 if pre == -1 else (dp[pre] + 1)  # pre==-1表示最后一块为0开始的
        if i > 0:
            dp[i] = max(dp[i], dp[i - 1])  # 两种情况取最大值
        map[xor] = i  # 更新异或和对应的位置
    return dp[len(arr) - 1]
