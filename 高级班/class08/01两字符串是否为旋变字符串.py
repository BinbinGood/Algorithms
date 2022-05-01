# 一个字符串可以分解成多种二叉树结构。如果str长度为 1，认为不可分解。
# 如果str长度为N(N>1)，左部分长度可以为 1~N-1，剩下的为右部分的长度。
# 左部分和右部分都可以按照同样的逻辑，继续分解。
# 形成的所有结构都是str的二叉树结构。
# 比如，字符串"abcd"，可以分解成以下五种结构，
# 任何一个str的二叉树结构中，如果两个节点有共同的父节点，那么这两个节点可以交换位
# 置，这两个节点叫作一个交换组。一个结构会有很多交换组，每个交换组都可以选择进行交
# 换或者不交换，最终形成一个新的结构，这个新结构所代表的字符串叫作 str的旋变字符串。
# 比如， 在上面的结构五中，交换组有a和b、ab和c、abc和d。如果让a和b的组交换；让ab和
# c的组不交 换；让abc和d的组交换，形成的结构如图
# 这个新结构所代表的字符串为"dbac"，叫作"abcd"的旋变字符串。也就是说，一个字符串
# str的旋变字符串是非常多的，str 可以形成很多种结构，每一种结构都有很多交换组，每
# 一个交换组都可以选择交换或者不交换，形成的每一个新的字符串都叫 str的旋变字符串。
# 给定两个字符串str1和str2，判断str2是不是str1的旋变字符串。


# 判断两个字符串长度是否一样，字符种类和数量是否一样
def sameTypeSameNumber(str1, str2):
    if len(str1) != len(str2):
        return False
    map = [0] * 256
    for i in range(len(str1)):
        map[ord(str1[i])] += 1
    for j in range(len(str2)):
        map[ord(str1[j])] -= 1
        if map[ord(str1[j])] < 0:
            return False
    return True


def isScramble1(str1, str2):
    if ((str1 is None) and (str2 is not None)) or ((str2 is None) and (str1 is not None)):
        return False
    if (str1 is None) and (str2 is None):
        return True
    if sameTypeSameNumber(str1, str2) is False:
        return False
    return process(str1, str2, 0, 0, len(str1))


# str1[L1~] 和str2[L2~] k个字符是否互为旋变字符串
def process(str1, str2, L1, L2, k):
    if k == 1:
        return str1[L1] == str2[L2]
    for leftpart in range(1, k):  # 可以取1到k-1
        if (process(str1, str2, L1, L2, leftpart) and
            process(str1, str2, L1 + leftpart, L2 + leftpart, k - leftpart)) \
                or (process(str1, str2, L1, L2 + k - leftpart, leftpart) and
                    process(str1, str2, L1 + leftpart, L2, k - leftpart)):
            return True
    return False


def isScramble2(str1, str2):
    if ((str1 is None) and (str2 is not None)) or ((str2 is None) and (str1 is not None)):
        return False
    if (str1 is None) and (str2 is None):
        return True
    if sameTypeSameNumber(str1, str2) is False:
        return False
    # l1,l2取值范围为0到len(str1)-1。k取值为1到len(str1)
    dp = [[[0] * (len(str1)) for i in range(len(str1))] for _ in range(len(str1) + 1)]
    # 首先填写第一层，因为k=0无效，所以从第一层开始填
    for l1 in range(len(str1)):
        for l2 in range(len(str1)):
            dp[1][l1][l2] = (str1[l1] == str2[l2])

    # 填写普遍位置
    for k in range(2, len(str1) + 1):
        for L1 in range(len(str1) - k + 1):
            for L2 in range(len(str1) - k + 1):
                dp[k][L1][L2] = False
                for leftpart in range(1, k):  # 可以取1到k-1
                    if (dp[leftpart][L1][L2] and dp[k - leftpart][L1 + leftpart][L2 + leftpart]) \
                            or (dp[leftpart][L1][L2 + k - leftpart] and dp[k - leftpart][L1 + leftpart][L2]):
                        dp[k][L1][L2] = True
                        break
    return dp[len(str1)][0][0]


test1 = "abcd"
test2 = "cdab"
print(isScramble1(test1, test2))
print(isScramble2(test1, test2))
test1 = "abcd"
test2 = "cadb"
print(isScramble1(test1, test2))
print(isScramble2(test1, test2))
test1 = "bcdebcdebcdebcdebcdebcdebcdebcdebcdebcdebcdebcdebcdebcdebcdebcdebcdebcdebcdebcdebcdebcde"
test2 = "ebcdeebcdebebcdebcdebcdecdebcbcdcdebcddebcbdebbbcdcdebcdeebcdebcdeebcddeebccdebcdbcdebcd"
# print(isScramble1(test1, test2))
print(isScramble2(test1, test2))
