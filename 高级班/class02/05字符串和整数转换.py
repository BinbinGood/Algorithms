# 一个 char 类型的数组 chs，其中所有的字符都不同。
# 例如，chs=['A', 'B', 'C', ... 'Z']，则字符串与整数的对应关系如下:
# A, B... Z, AA,AB...AZ,BA,BB...ZZ,AAA... ZZZ, AAAA...
# 1, 2...26,27, 28... 52,53,54...702,703...18278, 18279...
# 例如，chs=['A', 'B', 'C']，则字符串与整数的对应关系如下:
# A,B,C,AA,AB...CC,AAA...CCC,AAAA...
# 1, 2,3,4,5...12,13...39,40...
# 给定一个数组 chs，实现根据对应关系完成字符串与整数相互转换的两个函数。

# K伪进制
def str2int(chs, str1):
    if len(str1) == 0:
        return 0
    res = 0
    for i in range(len(str1) - 1, -1, -1):
        res += (ord(str1[i]) - ord('A') + 1) * pow(len(chs), len(str1) - 1 - i)
    return res


def int2str(chs, num):
    weishu = 0
    temp = num
    while temp != 0:
        temp = temp // len(chs)
        weishu += 1
    res = ['']*weishu



print(str2int(['A', 'B', 'C'], 'AAAA'))
