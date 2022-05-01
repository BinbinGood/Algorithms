# 给定一个整型数组 arr，代表数值不同的纸牌排成一条线。玩家 A 和玩家 B 依次拿走每张纸 牌，
# 规定玩家 A 先拿，玩家 B 后拿，但是每个玩家每次只能拿走最左或最右的纸牌，玩家 A 和 玩
# 家 B 都绝顶聪明。请返回最后获胜者的分数
def f(arr, i, j):
    if i == j:
        return arr[i]
    return max(arr[i] + s(arr, i + 1, j), arr[j] + s(arr, i, j - 1))


def s(arr, i, j):
    if i == j:
        return 0
    return min(f(arr, i + 1, j), f(arr, i, j - 1))


def win1(arr):
    return max(f(arr, 0, len(arr) - 1), s(arr, 0, len(arr) - 1))


# 严格表结构dp
def win2(arr):
    fdp = [[0] * len(arr) for _ in range(len(arr))]
    sdp = [[0] * len(arr) for _ in range(len(arr))]
    for j in range(len(arr)):
        fdp[j][j] = arr[j]
        for i in range(j - 1, -1, -1):
            fdp[i][j] = max(arr[i] + sdp[i + 1][j], arr[j] + sdp[i][j - 1])
            sdp[i][j] = min(fdp[i + 1][j], fdp[i][j - 1])

    return max(fdp[0][len(arr) - 1], sdp[0][len(arr) - 1])


if __name__ == "__main__":
    str1 = [1, 2, 100, 4]
    print(win1(str1))
    print(win2(str1))
