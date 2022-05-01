# 给定一个函数f，可以1～5的数字等概率返回一个。请加工出1～7的数字等概率
# 返回一个的函数g。
# 给定一个函数f，可以a～b的数字等概率返回一个。请加工出c～d的数字等概率
# 返回一个的函数g。
# 给定一个函数f，以p概率返回0，以1-p概率返回1。请加工出等概率返回0和1的
# 函数g
import random


def f():
    return random.randint(1, 6)


# 等概率产生01
def r01():
    res = f()
    while res == 3:
        res = f()
    return 1 if res > 3 else 0


def g():
    randomnum = r01() << 2
    randomnum += r01() << 1
    randomnum += r01()
    while randomnum > 6:
        randomnum = r01() << 2
        randomnum += r01() << 1
        randomnum += r01()
    return randomnum + 1


# 给定一个函数f，以p概率返回0，以1-p概率返回1。请加工出等概率返回0和1的
# 函数g
def fp():
    p = 0.75
    return 0 if random.random() > p else 1


def g01():
    r1 = fp()
    r2 = fp()
    while r1 == r2:
        r1 = fp()
        r2 = fp()
    return 0 if r1 == 0 else 1


if __name__ == "__main__":
    print(g())
    print("-------测试-------")
    cishu = [0] * 8
    for _ in range(100000):
        cishu[r01()] += 1
    print(cishu)
