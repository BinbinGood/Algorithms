# 把一个数字用中文表示出来。数字范围为 [0, 99999]。
# 为了方便输出，使用字母替换相应的中文，万W 千Q 百B 十S 零L。使用数字取代中
# 文数字注：对于 11 应该表示为 一十一(1S1)，而不是十一(S1)
# 输入描述：
# 数字 0（包含）到 99999（包含）。
# 输出描述：
# 用字母替换相应的中文，万W 千Q 百B 十S 零L
# 示例1:
# 输入
# 12001
# 输出
# 1W2QL1
danwei = ['L', 1]


def num1to9(num):
    if num < 1 or num > 9:
        return ''
    return str(num)


def num1to99(num, hasshi):  # 考虑习惯，11读作s1，而不是1s1
    if num < 1 or num > 99:
        return ''
    if num < 10:
        return num1to9(num)
    shi = num // 10
    if (hasshi is False) and shi == 1:
        return 'S' + num1to9(num % 10)
    else:
        return num1to9(shi) + 'S' + num1to9(num % 10)


def num1to999(num):
    if num < 1 or num > 999:
        return ''
    if num < 100:
        return num1to99(num, False)
    bai = num // 100
    res = num1to9(bai) + 'B'
    rest = num % 100
    if rest == 0:
        return res
    elif rest >= 10:
        res += num1to99(rest, True)
    else:
        res += 'L' + num1to9(rest)
    return res


def num1to9999(num):
    if num < 1 or num > 9999:
        return ''
    if num < 1000:
        return num1to999(num)
    qian = num // 1000
    res = num1to9(qian) + 'Q'
    rest = num % 1000
    if rest == 0:
        return res
    elif rest >= 100:
        res += num1to999(rest)
    else:
        res += 'L' + num1to99(rest, False)
    return res


def num1to99999999(num):
    if num < 1 or num > 99999999:
        return ''
    if num < 10000:
        return num1to9999(num)
    wan = num // 10000
    res = num1to9999(wan) + 'W'
    rest = num % 10000
    if rest == 0:
        return res
    elif rest >= 1000:
        res += num1to9999(rest)
    else:
        res += 'L' + num1to999(rest)
    return res


print(num1to99999999(1000001))
