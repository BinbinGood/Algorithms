# 在一个字符串中找到没有重复字符子串中最长的长度。
# 例如：
# abcabcbb没有重复字符的最长子串是abc，长度为3
# bbbbb，答案是b，长度为1
# pwwkew，答案是wke，长度是3
# 要求：答案必须是子串，"pwke" 是一个子字符序列但不是一个子字符串。

def Maxlongstr(str1):
    if len(str1) == 0:
        return 0
    map = [-1] * 256  # 要用数组代替哈希表
    maxlen = 0
    pre = -1
    for i in range(len(str1)):
        pre = max(pre, map[ord(str1[i])])  # 字符上次出现的位置和上一个字符最大长度对应位置，两者取位置最大值
        maxlen = max(maxlen, i - pre)  # 更新最大字符长度
        map[ord(str1[i])] = i  # 更新当前字符的位置
    return maxlen


str1 = 'abc'
print(Maxlongstr(str1))
