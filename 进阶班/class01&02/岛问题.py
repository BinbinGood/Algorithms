# 【题目】
# 一个矩阵中只有0和1两种值，每个位置都可以和自己的上、下、左、右 四个位置相连，如
# 果有一片1连在一起，这个部分叫做一个岛，求一个矩阵中有多少个岛?
# 【举例】
# 001010
# 111010
# 100100
# 000000
# 这个矩阵中有三个岛
def countIslands(contrix):
    if (len(contrix) < 0) or (len(contrix[0]) < 0) or (contrix is None):
        return 0
    res = 0
    for i in range(len(contrix)):
        for j in range(len(contrix[0])):
            if contrix[i][j] == 1:
                res += 1
                infect(contrix, i, j, len(contrix), len(contrix[0]))
    return res


def infect(contrix, i, j, m, n):
    if (i < 0) or (j < 0) or (j == n) or (i == m) or (contrix[i][j] != 1):
        return
    contrix[i][j] = 2
    infect(contrix, i + 1, j, m, n)
    infect(contrix, i, j + 1, m, n)
    infect(contrix, i - 1, j, m, n)
    infect(contrix, i, j - 1, m, n)


if __name__ == "__main__":
    m1 = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 1, 1, 1, 0, 1, 1, 1, 0],
          [0, 1, 1, 1, 0, 0, 0, 1, 0],
          [0, 1, 1, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 1, 1, 0, 0],
          [0, 0, 0, 0, 1, 1, 1, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0]]
    print(countIslands(m1))
