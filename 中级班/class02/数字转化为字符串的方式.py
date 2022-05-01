# 将给定的数转换为字符串，原则如下：1对应 a，2对应b，…..26对应z，例如12258
# 可以转换为"abbeh", "aveh", "abyh", "lbeh" and "lyh"，个数为5，编写一个函
# 数，给出可以转换的不同字符串的个数。

def Stringnum1(num):
    if num <= 0:
        return 0
    strnum = str(num)
    return process(strnum, 0)


# 将数字转化为字符的函数
# def num2str(num):
#     strnum = []
#     stack = []
#     while num:
#         stack.append(int(num % 10))
#         num = int(num / 10)
#     while stack:
#         strnum.append(stack.pop())
#     return strnum


def process(numstr, i):
    if i == len(numstr):
        return 1
    # 这样得到的时一个一个的字符，无法直接计算。
    if int(numstr[i]) == 0:  # 数字是0
        return 0
    elif i == len(numstr) - 1:  # 只剩下最后一个数字
        return process(numstr, i + 1)
    elif int(numstr[i]) * 10 + int(numstr[i + 1]) < 27:
        return process(numstr, i + 1) + process(numstr, i + 2)
    else:
        return process(numstr, i + 1)


def Stringnum2(num):
    if num <= 0:
        return 0
    strnum = str(num)
    dp = [0] * (len(strnum) + 1)
    dp[len(strnum)] = 1
    for i in range(len(strnum) - 1, -1, -1):
        if int(strnum[i]) == 0:
            dp[i] = 0
        elif i == len(strnum) - 1:
            dp[i] = getvalue(dp, i + 1)
        elif int(strnum[i]) * 10 + int(strnum[i + 1]) < 27:
            dp[i] = getvalue(dp, i + 1) + getvalue(dp, i + 2)
        else:
            dp[i] = getvalue(dp, i + 1)
    return dp[0]


def getvalue(dp, i):
    if i > len(dp):
        return 1
    return dp[i]


if __name__ == "__main__":
    num = 12258
    print(Stringnum1(num))
    print(Stringnum2(num))
