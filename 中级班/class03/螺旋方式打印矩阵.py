# 用螺旋的方式打印矩阵，比如如下的矩阵
# 0 1 2 3
# 4 5 6 7
# 8 9 10 11
# 打印顺序为：0 1 2 3 7 11 10 9 8 4 5 6
def Rotateprint(matrix):
    col = len(matrix)
    rol = len(matrix[0])  # 列
    a_x, a_y = 0, 0
    b_x, b_y = col - 1, rol - 1
    while b_x >= a_x and a_y <= b_y:
        printmatrix(matrix, a_x, a_y, b_x, b_y)
        a_x += 1
        a_y += 1
        b_x -= 1
        b_y -= 1


def printmatrix(matrix, a_x, a_y, b_x, b_y):
    if a_x == b_x:  # 在同一行
        while a_y != b_y + 1:
            print(matrix[a_x][a_y], end=' ')
            a_y += 1
    elif a_y == b_y:  # 在同一列
        while a_x != b_x + 1:  # 加1的目的是可以输出最后一个位置的值
            print(matrix[a_x][a_y], end=' ')
            a_x += 1
    else:  # 常规情况
        curx, cury = a_x, a_y
        while cury < b_y:
            print(matrix[curx][cury], end=' ')
            cury += 1
        while curx < b_x:
            print(matrix[curx][cury], end=' ')
            curx += 1
        while cury > a_y:
            print(matrix[curx][cury], end=' ')
            cury -= 1
        while curx > a_x:
            print(matrix[curx][cury], end=' ')
            curx -= 1


if __name__ == "__main__":
    matrix1 = [[0, 1, 2, 3],
               [4, 5, 6, 7],
               [8, 9, 10, 11]]
    Rotateprint(matrix1)
