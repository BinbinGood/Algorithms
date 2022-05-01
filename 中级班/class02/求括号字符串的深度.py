# 一个合法的括号匹配序列有以下定义:
# ①空串""是一个合法的括号匹配序列
# ②如果"X"和"Y"都是合法的括号匹配序列,"XY"也是一个合法的括号匹配序列
# ③如果"X"是一个合法的括号匹配序列,那么"(X)"也是一个合法的括号匹配序列
# ④每个合法的括号序列都可以由以上规则生成。
# 例如: "","()","()()","((()))"都是合法的括号序列
# 对于一个合法的括号序列我们又有以下定义它的深度:
# ①空串""的深度是0
# ②如果字符串"X"的深度是x,字符串"Y"的深度是y,那么字符串"XY"的深度为
# max(x,y) 3、如果"X"的深度是x,那么字符串"(X)"的深度是x+1
# 例如: "()()()"的深度是1,"((()))"的深度是3。牛牛现在给你一个合法的括号
# 序列,需要你计算出其深度。
def deep(s):
    if isvaild(s) is False:
        return 0
    maxdeep = 0
    count = 0
    for i in range(len(s)):
        if s[i] == '(':
            count += 1
            maxdeep = max(maxdeep, count)
        else:
            count -= 1
    return maxdeep


# 判断是否为合法括号字符串
def isvaild(s):
    if len(s) < 0:
        return False
    count = 0
    for i in range(len(s)):
        if s[i] == '(':
            count += 1
        else:
            count -= 1
    return True if count == 0 else False


# 求括号字符串的最长合法子串
def maxlength(s):
    dp = [0] * len(s)
    pre, res = 0, 0
    for i in range(1, len(s), 1):
        if s[i] == ')':
            pre = i - dp[i - 1] - 1
            if pre >= 0 and s[pre] == '(':
                dp[i] = dp[i - 1] + 2
                if pre > 0:
                    dp[i] += dp[pre - 1]
        res = max(res, dp[i])
    return res


if __name__ == "__main__":
    str1 = '()(())'
    print(maxlength(str1))
