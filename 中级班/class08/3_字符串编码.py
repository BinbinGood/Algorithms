# 在K数MP据算加法密扩和展数据题压目缩二中常需要对特殊的字符串进行编码。给定的字母表A由26个小写英文字母组成，即
# A={a, b...z}。该字母表产生的长序字符串是指定字符串中字母从左到右出现的次序与字母在字母表中出现
# 的次序相同，且每个字符最多出现1次。例如，a，b，ab，bc，xyz等字符串是升序字符串。对字母表A产生
# 的所有长度不超过6的升序字符串按照字典排列编码如下：a(1)，b(2)，c(3)……，z(26)，ab(27)，
# ac(28)……对于任意长度不超过16的升序字符串，迅速计算出它在上述字典中的编码。
# 输入描述：
# 第1行是一个正整数N，表示接下来共有N行，在接下来的N行中，每行给出一个字符串。输出描述：
# 输出N行，每行对应于一个字符串编码。
# 示例1:
# 输入
# 3
# a
# b
# ab
# 输出
# 1
# 2
# 27

# 以第i个字符开头，长度为long的所有字符串。有多少个
def f(i, long):
    sum = 0
    if long == 1:
        return 1
    for j in range(i + 1, 27):
        sum += f(j, long - 1)
    return sum


# 长度为long的字符串一共有多少个
def g(long):
    sum = 0
    for i in range(1, 27):
        sum += f(i, long)
    return sum


def kth(s):
    sum = 0
    for i in range(len(s)):  # 首先计算小于len(s)长度所有字符的总和
        sum += g(i)
    first = ord(s[0]) - ord('a') + 1  # 然后计算长度为len(s),首字母编号小于s[0]的字符个数
    for i in range(1, first):
        sum += f(i, len(s))
    pre = first
    for i in range(1, len(s)):
        cur = ord(s[i]) - ord('a') + 1
        for j in range(pre + 1, cur):  # 为了保证是升序字符串，所以必须用pre记录上一个字符，这样就知道后续字符的可能取值范围
            sum += f(j, len(s) - i)
        pre = cur
    return sum + 1


test = 'ac'
print(kth(test))
