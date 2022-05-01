# 判定一个由[a-z]字符构成的字符串和一个包含'.'和'*'通配符的字符串是否匹配。
# 通配符'.'匹配任意单一字符,'*'匹配任意多个字符包括0个字符。
# 字符串长度不会超过100，字符串不为空。
# 输入描述：
# 字符串 str 和包含通配符的字符串 pattern。1 <= 字符串长度 <= 100输出描述：
# true 表示匹配，false 表示不匹配

def ismatch(str1, exp):
    if len(str1) == 0 or len(exp) == 0:
        return False
    return process(str1, exp, 0, 0) if (isvaild(str1, exp)) else False


# 判断s,e是否符合要求
def isvaild(s, e):
    # s中不能有通配符
    for i in range(len(s)):
        if s[i] == '*' or s[i] == '.':
            return False
    for i in range(len(e)):
        # 出现连续两个‘*’ 判为False，或者开头为*
        if ((e[i] == '*') and (i == 0 or e[i - 1] == '*')):
            return False
    return True


# s[si:]能否被e[ei:]配出来
# 必须保证ei压中的不是 *
def process(s, e, si, ei):
    # base case
    if ei == len(e):
        return si == len(s)  # 当两者都走到最后为True
    # 可能性一，ei+1位置不是*
    # str[si]必须和exp[ri]配出来，并且后续能走通
    if (ei + 1 == len(e)) or (e[ei + 1] != '*'):
        return (si != len(s)) and (e[ei] == s[si] or e[ei] == '.') \
               and process(s, e, si + 1, ei + 1)  # si 有字符，和ei相等，且后续也能配出来
    # 可能性二，ei+1位置是*
    while (si != len(s)) and (e[ei] == s[si] or e[ei] == '.'):
        if process(s, e, si, ei + 2):
            return True
        si += 1
    return process(s, e, si, ei + 2)


# 方法二，利用dp表动态规划

# 测试
str1 = "abcd"
exp = "a..d"
print(ismatch(str1, exp))
