# 给定一个元素为非负整数的二维数组matrix，每行和每列都是从小到大有序的。
# 再给定一个非负整数aim，请判断aim是否在matrix中。

# 解法：从矩阵的右上角开始向左查询，遇到比aim小的数就向下查询，遇到比aim大的数就向左查询，重复步骤，直到走到尽头。

def aiminmatrix(matrix, aim):
    row = len(matrix[0])  # 列
    col = len(matrix)  # 行
    curcol, currow = 0, row - 1
    while 1:
        if matrix[curcol][currow] == aim:
            return True
        if currow < 0 or curcol == col:
            return False
        if matrix[curcol][currow] > aim:
            currow -= 1
        else:
            curcol += 1


if __name__ == "__main__":
    matrix1 = [[0, 1, 2, 3, 4, 5, 6],
               [10, 12, 13, 15, 16, 17, 18],
               [23, 24, 25, 26, 27, 28, 29],
               [44, 45, 46, 47, 48, 49, 50],
               [65, 66, 67, 68, 69, 70, 71],
               [96, 97, 98, 99, 100, 111, 122],
               [166, 176, 186, 187, 190, 195, 200],
               [233, 243, 321, 341, 356, 370, 380]]
    print(aiminmatrix(matrix1, 233))
