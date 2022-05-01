# 给定一个整型数组arr，代表数值不同的纸牌排成一条线。玩家A和玩家B依次拿走每张纸
# 牌，规定玩家A先拿，玩家B后拿，但是每个玩家每次只能拿走最左或最右的纸牌，玩家A
# 和玩家B都绝顶聪明。请返回最后获胜者的分数。
# 【举例】
# arr=[1,2,100,4]。
# 开始时，玩家A只能拿走1或4。如果开始时玩家A拿走1，则排列变为[2,100,4]，接下来
# 玩家 B可以拿走2或4，然后继续轮到玩家A...
# 如果开始时玩家A拿走4，则排列变为[1,2,100]，接下来玩家B可以拿走1或100，然后继
# 续轮到玩家A...
# 玩家A作为绝顶聪明的人不会先拿4，因为拿4之后，玩家B将拿走100。所以玩家A会先拿1，
# 让排列变为[2,100,4]，接下来玩家B不管怎么选，100都会被玩家 A拿走。玩家A会获胜，
# 分数为101。所以返回101。
# arr=[1,100,2]。
# 开始时，玩家A不管拿1还是2，玩家B作为绝顶聪明的人，都会把100拿走。玩家B会获胜，
# 分数为100。所以返回100。

def firsthand(arr, l, r):
    if l == r:
        return arr[l]
    return max((arr[l] + lasthand(arr, l + 1, r)), (arr[r] + lasthand(arr, l, r - 1)))


def lasthand(arr, l, r):
    if l == r:
        return 0
    return min(firsthand(arr, l + 1, r), firsthand(arr, l, r - 1))


def win1(arr):
    if arr is None or len(arr) == 0:
        return 0
    return max(firsthand(arr, 0, len(arr) - 1), lasthand(arr, 0, len(arr) - 1))


if __name__ == "__main__":
    str1 = [1, 2, 100, 4]
    print(win1(str1))
    str1 = [1, 100, 2]
    print(win1(str1))
