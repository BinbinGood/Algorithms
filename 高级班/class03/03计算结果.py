# 给定一个字符串str，str表示一个公式，公式里可能有整数、加减乘除符号和左右
# 括号，返回公式的计算结果。
# 【举例】
# str="48*((70-65)-43)+8*1"，返回-1816。
# str="3+1*4"，返回7。
# str="3+(1*4)"，返回7。
# 【说明】
# 1．可以认为给定的字符串一定是正确的公式，即不需要对str做公式有效性检查。
# 2．如果是负数，就需要用括号括起来，比如"4*(-3)"。但如果负数作为公式的开头
# 或括号部分的开头，则可以没有括号，比如"-3*4"和"(-3*4)"都是合法的。
# 3．不用考虑计算过程中会发生溢出的情况。

def strtocompute(str1):
    return process(str1, 0)[0]


def process(str1, i):
    stack = []
    pre = 0
    while i < len(str1) and str1[i] != ')':
        if ord('9') >= ord(str1[i]) >= ord('0'):
            pre = pre * 10 + ord(str1[i]) - ord('0')
            i += 1
        elif str1[i] != '(':
            addnum(stack, pre)
            stack.append(str1[i])
            i += 1
            pre = 0
        else:  # 遇到左括号
            bra = process(str1, i + 1)
            pre = bra[0]
            i = bra[1] + 1
    addnum(stack, pre)
    return [getnum(stack), i]


def addnum(stack, num):
    if stack:
        top = stack.pop()
        if top == '+' or top == '-':
            stack.append(top)
        else:
            cur = stack.pop()
            if (top == '*'):
                num = cur * num
            else:
                num = cur // num
    stack.append(num)


def getnum(queue):
    res = 0
    add = True
    while queue:
        cur = queue.pop(0)  # 在计算栈中数据的总和时，从头开始加减。不然会出错
        if cur == '+':
            add = True
        elif cur == '-':
            add = False
        else:
            res += (cur if add else (-cur))
    return res


str1 = "48*((70-65)-43)+8*1"
print(strtocompute(str1))
