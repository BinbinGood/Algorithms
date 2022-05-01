# 针对如斐波那契数列一样的无条件转移的递归套路
# 1 1 2 3 5 8 13

# 字符串只由'0'和'1'两种字符构成，
# 当字符串长度为1时，所有可能的字符串为"0"、"1"；
# 当字符串长度为2时，所有可能的字符串为"00"、"01"、"10"、"11"；
# 当字符串长度为3时，所有可能的字符串为"000"、"001"、"010"、"011"、"100"、
# "101"、"110"、"111"
# ...
# 如果某一个字符串中，只要是出现'0'的位置，左边就靠着'1'，这样的字符串叫作达
# 标字符串。
# 给定一个正数N，返回所有长度为N的字符串中，达标字符串的数量。
# 比如，N=3，返回3，因为只有"101"、"110"、"111"达标。

# 此题目可以用斐波那契额套路解


def f(n):
    if n == 1 or n == 2:
        return 1
    matrix = [[1, 1],
              [1, 0]]
    res = getmatrixpow(matrix, n - 2)
    return res[0][0] + res[1][0]


def getmatrixpow(matrix, n):
    res = [[0] * len(matrix[0]) for _ in range(len(matrix))]
    for i in range(len(res)):
        res[i][i] = 1
    t = matrix
    while n != 0:
        if n & 1 != 0:
            res = mulimatrix(res, t)

        t = mulimatrix(t, t)
        n >>= 1
    return res


def mulimatrix(matrix1, matrix2):
    res = [[0] * len(matrix2[0]) for _ in range(len(matrix1))]
    for i in range(len(res)):
        for j in range(len(res[0])):
            for k in range(len(matrix2)):
                res[i][j] += matrix1[i][k] * matrix2[k][j]

    return res


print(f(7))
