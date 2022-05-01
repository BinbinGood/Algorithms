# 如果一个字符串为str，把字符串str前面任意的部分挪到后面形成的字符串叫
# 作str的旋转词。比如str="12345"，str的旋转词有"12345"、"23451"、
# "34512"、"45123"和"51234"。给定两个字符串a和b，请判断a和b是否互为旋转
# 词。
# 比如：
# a="cdab"，b="abcd"，返回true。
# a="1ab2"，b="ab12"，返回false。
# a="2ab1"，b="ab12"，返回true。

def isxuanzhuan(a, b):
    str1 = a + a
    return KMP(str1, b)


def KMP(str1, str2):
    if len(str1) < len(str2):
        return False
    i1, i2 = 0, 0
    next = getnextarr(str2)
    while i1 < len(str1) and i2 < len(str2):
        if str1[i1] == str2[i2]:
            i1 += 1
            i2 += 1
        elif i2 == 0:
            i1 += 1
        else:
            i2 = next[i2]
    if i2 == len(str2):
        return True
    else:
        return False


def getnextarr(str2):
    next = [None] * len(str2)
    next[0] = -1
    next[1] = 0
    i = 2
    cn = 0
    while i < len(str2):
        if str2[i - 1] == str2[cn]:
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
    a, b = '1ab2', 'b211'
    print(isxuanzhuan(a, b))
