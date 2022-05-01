# N皇后问题是指在N*N的棋盘上要摆N个皇后，要求任何两个皇后不同行、不同列，
# 也不在同一条斜线上。
# 给定一个整数n，返回n皇后的摆法有多少种。
# n=1，返回1。
# n=2或3，2皇后和3皇后问题无论怎么摆都不行，返回0。
# n=8，返回92。

def NQueens(num):
    if num < 1:
        return 0
    record = [None] * num
    result = []
    process(0, record, num, result)
    return result


# record 存放的是前i-1行皇后的位置,n表示总的行数
# i表示寻找此行应该放的位置
def process(i, record, n, res):
    if i == n:
        return res.append(record[:])
    for j in range(n):
        if isvaild(record, i, j):
            record[i] = j
            process(i + 1, record, n, res)
    return res


# 验证第i行皇后放在第j列是否有效
def isvaild(record, i, j):
    for h in range(i):
        # 属于同一列或者同一斜线上（呈45度角），则返回False
        if (j == record[h]) or (abs(record[h] - j) == abs(i - h)):
            return False
    return True


if __name__ == "__main__":
    num = 8
    result = NQueens(num)
    print(result)
    print(len(result))
