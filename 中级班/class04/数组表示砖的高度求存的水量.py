# 给定一个数组arr，已知其中所有的值都是非负的，将这个数组看作一个容器，
# 请返回容器能装多少水
# 比如，arr = {3，1，2，5，2，4}，根据值画出的直方图就是容器形状，该容
# 器可以装下5格水
# 再比如，arr = {4，5，1，3，2}，该容器可以装下2格水

# 方法一，计算每个位置i，其左侧最大值和右侧最大值，则i位置可以存的水为左右最大值较小的一个-i位置的高度

# 方法二，利用左侧最大值，右侧最大值和LR两个指针，进行遍历
def getwater(arr):
    if len(arr) < 3:
        return 0
    leftmax = arr[0]
    rightmax = arr[len(arr) - 1]
    Lindex = 1
    Rindex = len(arr) - 2
    water = 0
    while Lindex < Rindex:
        if leftmax < rightmax:
            water += max(0, leftmax - arr[Lindex])
            leftmax = max(leftmax, arr[Lindex])
            Lindex += 1
        else:
            water += max(0, rightmax - arr[Rindex])
            rightmax = max(rightmax, arr[Rindex])
            Rindex -= 1
    return water


if __name__ == "__main__":
    # arr = [3,1,2,5,2,4]
    arr = [4, 5, 1, 3, 2]
    print(getwater(arr))
