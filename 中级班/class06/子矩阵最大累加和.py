# 给定一个整型矩阵，返回子矩阵的最大累计和。

def matrixMaxsum(matrix):
    cur = 0
    maxres = matrix[0][0]
    for i in range(len(matrix)):
        s = [0] * len(matrix[0])
        for j in range(i, len(matrix)):
            cur = 0
            for k in range(len(s)):
                s[k] += matrix[j][k]
                cur += s[k]
                maxres = max(maxres, cur)
                cur = 0 if cur < 0 else cur
    return maxres


matrix1 = [[-5, 3, 6, 4],
           [-7, 9, -5, 3],
           [-10, 1, -200, 4]]
print(matrixMaxsum(matrix1))
