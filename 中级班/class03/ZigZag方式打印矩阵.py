# 用zigzag的方式打印矩阵，比如如下的矩阵
# 0 1 2 3
# 4 5 6 7
# 8 9 10 11
# 打印顺序为：0 1 4 8 5 2 3 6 9 10 7 11

def ZigzagPrint(matrix):
    col = len(matrix)
    rol = len(matrix[0])  # 列
    a_x, a_y = 0, 0  # 通过指针a和b记录每次要打印斜行的左上角和右小角坐标。调用打印函数，打印他们中间的值
    b_x, b_y = 0, 0
    upflag = False
    while a_x < col:
        printmatrix(matrix, a_x, a_y, b_x, b_y, upflag)
        if a_y == rol - 1:
            a_x += 1
        else:
            a_y += 1
        if b_x == col - 1:
            b_y += 1
        else:
            b_x += 1
        upflag = ~upflag


def printmatrix(matrix, a_x, a_y, b_x, b_y, upflag):
    if upflag:
        while b_x != a_x - 1:
            print(matrix[b_x][b_y], end=' ')
            b_x -= 1
            b_y += 1
    else:
        while a_x != b_x + 1:
            print(matrix[a_x][a_y], end=' ')
            a_x += 1
            a_y -= 1


if __name__ == "__main__":
    matrix1 = [[0, 1, 2, 3],
               [4, 5, 6, 7],
               [8, 9, 10, 11]]
    ZigzagPrint(matrix1)
