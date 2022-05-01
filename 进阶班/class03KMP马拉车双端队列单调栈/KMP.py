# 字符串str1和str2，str1是否包含str2，如果包含返回str2在str1中开始的位置。
def KMP(str1, str2):
    if (str1 is None) or (str2 is None) or (len(str2) < 1) or (len(str1) < len(str2)):
        return -1
    i1 = i2 = 0
    nextstr = getNextArray(str2)
    while (i1 < len(str1)) and (i2 < len(str2)):
        if str1[i1] == str2[i2]:
            i1 += 1
            i2 += 1
        elif i2 == 0:
            i1 += 1
        else:
            i2 = nextstr[i2]
    # 判断是否为i2走到末尾
    if i2 == len(str2):
        return i1 - i2
    else:
        return -1


def getNextArray(str):
    if len(str) == 1:
        return [-1]
    next = [None] * len(str)
    next[0] = -1
    next[1] = 0
    i = 2
    cn = 0
    while i < len(next):
        if str[i - 1] == str[cn]:
            next[i] = cn + 1
            i += 1
            cn += 1
        elif cn > 0:
            cn = next[cn]
        else:
            next[i] = 0
            i += 1
    return next


if __name__ == "__main__":
    str1 = 'abbcabbtd'
    str2 = 'abbs'
    print(KMP(str1, str2))
