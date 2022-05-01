# 确保输入n不是0就是1的情况下，输入1->0，0->1
# ^:异或符号
def flip(n):
    return n ^ 1


# 符号函数，将32位数右移31位（可以和1与一下，防止出错），得到符号位，取反以后即可得到姐结果
# 输入非负数，返回1
# 输入负数，返回0
def sign(n):
    return flip((n >> 31) & 1)


# 可能溢出
def getMax1(a, b):
    c = a - b
    scA = sign(c)  # a-b为非负，scA为1；a-b为负，scA为0
    scB = flip(scA)  # scA为0,scB为1；scA为1，scB为0
    return scA * a + scB * b


# 改进版本，可以应对溢出问题
# 返回a,有两种情况：1）ab符号相同，此时肯定不会溢出，看a-b的符号
# 2）ab符号不同，此时看a的符号
def getMax2(a, b):
    c = a - b
    sa = sign(a)
    sb = sign(b)
    sc = sign(c)
    disab = sa ^ sb  # ab符号相同为0，不同为1
    sameab = flip(disab)  # a和b的符号不一样为0，一样为1
    returna = disab * sa + sameab * sc
    returnb = flip(returna)  # 取反
    return returna * a + returnb * b


if __name__ == "__main__":
    print(getMax2(-1, 0))
