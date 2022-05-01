# 请注意区分子串和子序列的不同，给定两个字符串str1和str2，求两个字符串的最长公
# 共子串。
# 动态规划空间压缩的技巧讲解

def Maxlongstr(str1, str2):
    res = 0
    end = 0
    i = 0  # 从右上角开始
    j = len(str2) - 1
    while i < len(str1) and j >= 0:
        curi = i
        curj = j
        t = 0
        while curi < len(str1) and curj < len(str2):
            if str1[curi] != str2[curj]:
                t = 0
            else:
                t += 1
            if t > res:
                res = t
                end = curi
            curi += 1
            curj += 1
        if j > 0:
            j -= 1
        else:
            i += 1
    return (res, str1[end - res + 1:end + 1])


str1 = "ABC1234567DEFG"
str2 = "HIJKL1234567MNOP"
print(Maxlongstr(str1, str2))

