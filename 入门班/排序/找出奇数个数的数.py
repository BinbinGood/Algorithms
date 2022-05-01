# 一个数组中有一种数出现了奇数次，其他数都出现了偶数次，怎么找到这一个数
def findoneoddnum(arrs):
    eor = 0
    for i in range(len(arrs)):
        eor = eor ^ arrs[i]
    print(f"该奇数为：{eor}")


# 一个数组中有两种数出现了奇数次，其他数都出现了偶数次，怎么找到这两个数
def findtwooddnum(arrs):
    eor = 0
    eohasone = 0
    for i in range(len(arrs)):
        eor = eor ^ arrs[i]
    rightone = eor & ((~eor) + 1)  # 提取eor数最右边那一位的1
    for i in range(len(arrs)):
        if arrs[i] & rightone == 0:
            eohasone = eohasone ^ arrs[i]
    print(f"这两个奇数为：{eohasone}和{eor^eohasone}")


if __name__ == "__main__":
    # findoneoddnum([2,2,3,3,3,3,4,4,4,5,5,6,6])
    findtwooddnum([1,1,1,3,2,2,3,3,4,4,5,5,6,6])