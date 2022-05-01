# 给定一个长度为偶数的数组arr，长度记为2*N。前N个为左部分，后N个为右部分。
# arr就可以表示为{L1,L2,..,Ln,R1,R2,..,Rn}，
# 请将数组调整成{R1,L1,R2,L2,..,Rn,Ln}的样子。

# 数组的长度为Long,调整前的位置是i，返回调整之后的位置
# 下标不从o开始，从1开始
def modifyIndex(i, long):
    return (2 * i) % (long + 1)


# 主函数
# 数组必须不为空，且长度为偶数
def shuffle(arr):
    if (len(arr) != 0) and (len(arr) & 1 == 0):
        shuffle1(arr, 0, len(arr) - 1)


# 在arr[l~r]上做完美洗牌的调整
def shuffle1(arr, l, r):
    # 切成一块一块的解决，每一块长度满足（3^k-1）
    while r - l + 1 > 0:
        long = r - l + 1  # 数组长度
        base = 3
        k = 1
        # 计算小于等于Long并且是离long最近的，满足(3^k)-1的数
        # 也就是找到最大的K，满足3^k <= long+1
        while base <= (long + 1) // 3:
            # (long+1)//3是因为要找小于等于的数，循环结束时刚好超过临界值，//3，此时的值刚好满足条件
            base *= 3
            k += 1
        # 当前要解决长度为base-1的块（(3^k)-1），一半就是再除2
        half = (base - 1) // 2
        # 找到l到r的中点位置
        mid = (l + r) // 2
        # 要旋转的左部分为[L + half...mid], 右部分为arr[mid + 1..mid + half]
        # 注意在这里，arr下标是从0开始的
        rotate(arr, l + half, mid, mid + half)
        # 旋转完成后，从L开始算起，长度为base - 1的部分进行下标连续推
        cycles(arr, l, base - 1, k)
        # 解决了前base - 1的部分，剩下的部分继续处理
        l = l + base - 1


# 从start位置开始，往右long的长度这一段，做下标连续推
# 出发位置依次为1,3,9~
def cycles(arr, start, long, k):
    # 找到每一个出发位置trigger，一共k个
    # 每一个trigger都进行下标连续推
    # 出发位置是从1开始算的，而数组下标是从0开始算的，所以要-1.
    i, trigger = 0, 1
    while i < k:
        prevalue = arr[trigger + start - 1]
        cur = modifyIndex(trigger, long)
        while cur != trigger:  # 循环结束的条件，回到原来的位置
            temp = arr[cur + start - 1]
            arr[cur + start - 1] = prevalue
            prevalue = temp
            cur = modifyIndex(cur, long)  # 计算新的位置
        arr[cur + start - 1] = prevalue

        i += 1
        trigger *= 3  # 下一个触发点


# 将arr,L到M为左部分，M+1到R为右部分，左右两部分互换
def rotate(arr, l, m, r):
    reverse(arr, l, m)
    reverse(arr, m + 1, r)
    reverse(arr, l, r)


# 将L到R做逆序调整
def reverse(arr, l, r):
    while l < r:
        temp = arr[l]
        arr[l] = arr[r]
        arr[r] = temp
        l += 1
        r -= 1


arr = [1, 2, 3, 4, 5, 6, 7, 8]
shuffle(arr)
print(arr)
