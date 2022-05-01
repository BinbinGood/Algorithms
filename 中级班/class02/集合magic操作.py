# 给一个包含n个整数元素的集合a，一个包含m个整数元素的集合b。
# 定义magic操作为，从一个集合中取出一个元素，放到另一个集合里，且操作过
# 后每个集合的平均值都大大于于操作前。
# 注意以下两点：
# 1）不可以把一个集合的元素取空，这样就没有平均值了
# 2）值为x的元素从集合b取出放入集合a，但集合a中已经有值为x的元素，则a的
# 平均值不变（因为集合元素不会重复），b的平均值可能会改变（因为x被取出
# 了）
# 问最多可以进行多少次magic操作？

def Maxmagicways(a, b):
    if len(a) <= 0 or len(b) <= 0:
        return 0
    asum, bsum = 0, 0
    for i in a:
        asum += i
    for i in b:
        bsum += i
    amean, bmean = getmean(asum, len(a)), getmean(bsum, len(b))
    if amean == bmean:
        return 0
    if amean > bmean:
        bigarr = a
        bigsum = asum
        smallarr = b
        smallsum = bsum
    else:
        bigarr = b
        bigsum = bsum
        smallarr = a
        smallsum = asum

    hashset = set()
    for i in smallarr:
        hashset.add(i)
    bigsize = len(bigarr)
    smallsize = len(smallarr)
    ops = 0
    bigarr.sort()
    for cur in bigarr:
        if getmean(smallsum, smallsize) < cur < getmean(bigsum, bigsize) and (cur not in hashset):
            bigsum -= cur
            smallsum += cur
            bigsize -= 1
            smallsize += 1
            hashset.add(cur)
            ops += 1
    return ops


def getmean(sumset, size):
    return sumset / size


if __name__ == "__main__":
    arr1 = [1, 2, 5]
    arr2 = [2, 3, 4, 5]
    print(Maxmagicways(arr1, arr2))
