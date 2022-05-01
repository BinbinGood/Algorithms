# 假设s和m初始化，s = "a"; m = s;
# 再定义两种操作，第一种操作：
# m = s;
# s = s + s;
# 第二种操作：
# s = s + m;
# 求最小的操作步骤数，可以将s拼接到长度等于n

def Minops(n):
    if n < 2:
        return 0
    if isprim(n):
        return n - 1
    sum, count = 0, 0
    for i in range(2, n, 1):
        while n % i == 0:
            sum += i
            count += 1
            n /= i
    return sum - count


def isprim(n):
    if n < 2:
        return False
    sqrt = int(pow(n, 0.5))  # 第二种方法是利用非质数一定有一对约数，一个大于平方根，一个小与平方跟。所以只需要判断2~平方根即可
    for i in range(2, sqrt + 1, 1):  # 第一种方法就是判断一个数是否能被比它小的数整除
        if n % i == 0:
            return False
    return True


if __name__ == "__main__":
    print(Minops(5))
