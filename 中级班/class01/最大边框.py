# 给定一个N*N的矩阵matrix，只有0和1两种值，返回边框全是1的最大正方形的边
# 长长度。
# 例如:
# 01111
# 01001
# 01001
# 01111
# 01011
# 其中边框全是1的最大正方形的大小为4*4，所以返回4。
import random


def MaxSide1(matrix):
    if len(matrix) == 0 or (len(matrix) != len(matrix[0])):
        return 0
    N = len(matrix)
    maxborder = 1
    for cow in range(N):  # 遍历行
        for row in range(N):  # 遍历列
            for s in range(min(N - cow, N - row), 0, -1):  # 遍历边长
                if isOneBorder(matrix, cow, row, s):
                    maxborder = max(maxborder, s)
                    break
    return maxborder


# 此函数判断matrix中，以cow,row为左上角点，s为边长的正方形是否边框全为1
def isOneBorder(matirx, cow, row, s):
    for i in range(row, row + s, 1):
        if matirx[cow][i] != 1 or matirx[cow + s - 1][i] != 1:
            return False
    for j in range(cow, cow + s, 1):
        if matirx[j][row] != 1 or matirx[j][row + s - 1] != 1:
            return False
    return True


def MaxSide2(matrix):
    if len(matrix) == 0 or (len(matrix) != len(matrix[0])):
        return 0
    N = len(matrix)
    helpright = [[0] * N for _ in range(N)]
    helpdown = [[0] * N for _ in range(N)]
    setBorderMap(matrix, helpright, helpdown)
    maxborder = 1
    for cow in range(N):  # 遍历行
        for row in range(N):  # 遍历列
            for s in range(min(N - cow, N - row), 0, -1):  # 遍历边长
                if helpright[cow][row] >= s and helpdown[cow][row] >= s \
                        and helpright[cow + s - 1][row] >= s and helpdown[cow][row + s - 1] >= s:
                    maxborder = max(maxborder, s)
                    break
    return maxborder


# 预处理矩阵
# down计算每个元素下边连续1的个数
# right计算每个元素右边连续1的个数
def setBorderMap(matrix, right, down):
    if matrix[len(matrix) - 1][len(matrix[0]) - 1] == 1:
        right[len(matrix) - 1][len(matrix[0]) - 1] = 1
        down[len(matrix) - 1][len(matrix[0]) - 1] = 1
    for cow in range(len(matrix) - 2, -1, -1):
        if matrix[cow][len(matrix[0]) - 1] == 1:
            right[cow][len(matrix[0]) - 1] = 1
            down[cow][len(matrix[0]) - 1] = down[cow + 1][len(matrix[0]) - 1] + 1
    for row in range(len(matrix[0]) - 2, -1, -1):
        if matrix[len(matrix) - 1][row] == 1:
            down[len(matrix) - 1][row] = 1
            right[len(matrix) - 1][row] = right[len(matrix) - 1][row + 1] + 1
    for cow in range(len(matrix) - 2, -1, -1):
        for row in range(len(matrix[0]) - 2, -1, -1):
            if matrix[cow][row] == 1:
                right[cow][row] = right[cow][row + 1] + 1
                down[cow][row] = down[cow + 1][row] + 1


# 测试使用
def Randommatrix(N):
    matrix = []
    for i in range(N):
        row = []
        for j in range(N):
            row.append(random.randint(0, 2))
        matrix.append(row)
    return matrix


if __name__ == "__main__":
    matrix1 = [[0, 1, 1, 1, 1],
               [0, 0, 0, 1, 0],
               [0, 1, 1, 1, 0],
               [0, 1, 0, 1, 1],
               [0, 1, 0, 1, 0]]
    print(MaxSide1(matrix1))

    print("---------对数器--------")
    for _ in range(1000):
        matrix1 = Randommatrix(10)
        if MaxSide1(matrix1) != MaxSide2(matrix1):
            print("出错")
            break
