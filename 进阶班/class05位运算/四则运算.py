# 加法
def add1(a, b):
    sum = int(a)
    while b != 0:
        sum = int(a ^ b)  # 异或保存无进位相加信息
        b = int((a & b) << 1)  # 与运算左移一位，保存进位信息,当进位信息位0时，表示运算结束
        a = int(sum)
    return sum


# 取反
def negnum(num):
    if num == 0:
        return 0
    return add1(~num, 1)


# 减法
def minus(a, b):
    if b == 0:
        return a
    b = negnum(b)
    return add1(a, b)


# 乘法
def multi(a, b):
    res = 0
    while b != 0:
        if b & 1 != 0:
            res = add1(res, a)
        a <<= 1
        b >>= 1
    return res


# 除法
def div(a, b):
    x, y = a, b
    if a < 0:
        x = negnum(a)
    if b < 0:
        y = negnum(b)
    res = 0
    for i in range(31, -1, -1):
        if (x >> i) >= y:
            res |= (1 << i)
            x = minus(x, y << i)
    if (a < 0 and b < 0) or (a >= 0 and b >= 0):
        return res
    else:
        return negnum(res)


class qita():

    def minus(self, a: int, b: int) -> int:
        return a + (-b)

    # 求num//2，返回商和余数
    def divideBy2(self, num) -> (int, int):
        res = 0
        while res < self.minus(num, res):
            half = 1
            while True:
                if res + half + half < self.minus(num, (res + half + half)):
                    half = half + half
                else:
                    break
            res = res + half
        if res == self.minus(num, res):
            return (res, 0)
        else:
            return (self.minus(res, 1), 1)

    def multiply(self, a: int, b: int) -> int:
        # 处理符号
        sign = True
        if a < 0:
            sign = not sign
            a = -a
        if b < 0:
            sign = not sign
            b = -b
        # 用较小的数做乘数
        if a < b:
            a, b = b, a
        # 循环每一轮做分解， `a * b = (a * 2) * (b // 2) + a * (b % 2)`
        remainder = 0  # 保存余数得累加和
        while b > 1:
            # b = b // 2, r = b % 1
            b, r = self.divideBy2(b)
            if r == 1:
                remainder = remainder + a
            a = a + a
        a = a + remainder
        if sign:
            return a
        return -a


if __name__ == "__main__":
    # print(bin(2))
    # print(bin(-1))
    # print(bin(2**32+(-1)))
    # print(qp.divide(4, -2))
    # print(minus(2, 1))
    # print(multi(-2, 1))
    # print(div(4,2))
    qita = qita()
    print(qita.divideBy2(7))
