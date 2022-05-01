# 给定一个正方形矩阵，只用有限几个变量，实现矩阵中每个位置的数顺时针转动
# 90度，比如如下的矩阵
# 0 1 2 3
# 4 5 6 7
# 8 9 10 11
# 12 13 14 15
# 矩阵应该被调整为：
# 12 8 4 0
# 13 9 5 1
# 14 10 6 2
# 15 11 7 3

def Rotatematrix(matrix):
    col = len(matrix)
    rol = len(matrix[0])  # 列
    a_x, a_y = 0, 0
    b_x, b_y = col - 1, rol - 1
    while b_x >= a_x:
        rotateedgematrix(matrix, a_x, a_y, b_x, b_y)
        a_x += 1
        a_y += 1
        b_x -= 1
        b_y -= 1


def rotateedgematrix(matrix, a_x, a_y, b_x, b_y):
    for i in range(b_y - a_y):
        temp = matrix[b_x - i][a_y]
        matrix[b_x - i][a_y] = matrix[b_x][b_y - i]
        matrix[b_x][b_y - i] = matrix[a_x + i][b_y]
        matrix[a_x + i][b_y] = matrix[a_x][a_y + i]
        matrix[a_x][a_y + i] = temp


if __name__ == "__main__":
    matrix1 = [[0, 1, 2, 3],
               [4, 5, 6, 7],
               [8, 9, 10, 11],
               [12, 13, 14, 15]]
    print(matrix1)
    Rotatematrix(matrix1)
    print(matrix1)
