# 给定两个字符串，记为start和to，再给定一个字符串列表list，list中一定包含to
# list中没有重复字符串，所有的字符串都是小写的。
# 规定：
# start每次只能改变一个字符，最终的目标是彻底变成to，但是每次变成的新字符串必须在list
# 中存在。
# 请返回所有最短的变换路径。
# 【举例】
# start="abc",end="cab",list={"cab","acc","cbc","ccc","cac","cbb","aab","abb"}
# 转换路径的方法有很多种，但所有最短的转换路径如下:
# abc -> abb -> aab -> cab
# abc -> abb -> cbb -> cab
# abc -> cbc -> cac -> cab
# abc -> cbc -> cbb -> cab

def findMinPaths(start, end, list):
    list.append(start)
    nexts = getNexts(list)
    distances = getDistances(start, nexts)
    pathlist = []
    res = []
    getShortPaths(start, end, nexts, distances, pathlist, res)
    return res


def getNexts(words):
    # 将List放入哈希表中
    hashset = set(words)
    hashnexts = dict()
    # 为每个元素创建一个nexts的映射
    for i in range(len(words)):
        hashnexts[words[i]] = getNext(words[i], hashset)
    return hashnexts


def getNext(word, hashset):
    res = []
    # 对每一个位置尝试26个字符
    for cur in range(ord('a'), ord('z') + 1):
        for i in range(len(word)):
            # 当前字符可以进行转换
            if word[i] != chr(cur):
                temp = word
                word = word[:i] + chr(cur) + word[i + 1:]
                # 判断转换后的字符是否在哈希表中
                if word in hashset:
                    res.append(word)
                # 恢复原来的字符
                word = temp
    return res


# 此处本质是以后深度优先遍历
def getDistances(start, nexts):
    distances = dict()
    distances[start] = 0
    queue = [start]
    hashset = set()
    hashset.add(start)
    while queue:
        cur = queue.pop(0)
        for curstr in nexts[cur]:
            if curstr not in hashset:
                distances[curstr] = distances[cur] + 1
                queue.append(curstr)
                hashset.add(curstr)
    return distances


def getShortPaths(cur, to, nexts, distances, solution, res):
    solution.append(cur)
    if to == cur:
        res.append(solution[:])  # 此处必须是复制的路径，不然最终得到的是空列表
    else:
        for next in nexts[cur]:
            if distances[next] == distances[cur] + 1:
                getShortPaths(next, to, nexts, distances, solution, res)
    solution.pop()


start = 'abc'
end = 'cab'
list1 = ["abc", "cab", "acc", "cbc", "ccc", "cac", "cbb", "aab", "abb"]
res = findMinPaths(start, end, list1)
# 打印最短路径
for obj in res:
    for cur in obj:
        print(cur, end='->')
    print()
