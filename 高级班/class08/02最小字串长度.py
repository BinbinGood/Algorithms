# 给定字符串str1和str2，求str1的子串中含有str2所有字符的最小子串长度
# 【举例】
# str1="abcde"，str2="ac"
# 因为"abc"包含 str2 所有的字符，并且在满足这一条件的str1的所有子串中，"abc"是
# 最短的，返回3。
# str1="12345"，str2="344"
# 最小包含子串不存在，返回0。
def minstr(str1, str2):
    if len(str2) == 0 or (str2 is None):
        return 0
    if len(str1) < len(str2):
        return 0
    hashmap = [0] * 256
    all = len(str2)
    for i in range(len(str2)):
        hashmap[ord(str2[i])] += 1
    l, r = 0, 0
    minres = pow(10, 4)
    while r < len(str1):
        hashmap[ord(str1[r])] -= 1
        if hashmap[ord(str1[r])] >= 0:  # 表明此字符为str2中出现过的字符
            all -= 1
        if all == 0:  # 窗口左边开始缩
            while hashmap[ord(str1[l])] < 0:
                hashmap[ord(str1[l])] += 1
                l += 1
            minres = min(minres, r - l + 1)
            all += 1
            hashmap[ord(str1[l])] += 1
        r += 1
    return minres if minres != pow(10, 4) else 0


str1 = "aaaabbcacbba"
str2 = "babca"
print(minstr(str1, str2))
