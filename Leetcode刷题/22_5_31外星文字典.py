# 现有一种使用英语字母的外星文语言，这门语言的字母顺序与英语顺序不同。
#
# 给定一个字符串列表 words ，作为这门语言的词典，words 中的字符串已经 按这门新语言的字母顺序进行了排序 。
#
# 请你根据该词典还原出此语言中已知的字母顺序，并 按字母递增顺序 排列。若不存在合法字母顺序，返回 "" 。若存在多种可能的合法字母顺序，返回其中 任意一种 顺序即可。
#
# 字符串 s 字典顺序小于 字符串 t 有两种情况：
#
# 在第一个不同字母处，如果 s 中的字母在这门外星语言的字母顺序中位于 t 中字母之前，那么 s 的字典顺序小于 t 。
# 如果前面 min(s.length, t.length) 字母都相同，那么 s.length < t.length 时，s 的字典顺序也小于 t
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/Jf1JuT
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# str1 = 'absdef'
# arr1 = [1, 2, 3, 4, 5]
# hashmap = {}
# for x, y in zip(str1, arr1):
#     hashmap[x] = y
# print(hashmap)
# for i in hashmap:
#     print(i,end=',')
from itertools import pairwise


class Solution:
    def alienOrder(self, words) -> str:
        g = {}  # 保存了每个字母和对应的比其小的字母
        for c in words[0]:  # 初始化第一个单词的所有字母
            g[c] = []
        for s, t in pairwise(words):  # 相邻两个单词为一对
            for c in t:  # 为每一对单词后面那个单词的每个字母设置默认为空列表
                g.setdefault(c, [])
            for u, v in zip(s, t):  #
                if u != v:  # 遇到第一个不相等的字母，则前面那个字母一定比后面那个字母小
                    g[u].append(v)
                    break
            else:  # 当for循环正常结束时，则会执行这个else。只有break跳出时才不执行。
                # 如果for正常结束，表示min(len(s),len(t))的字符全一样，但是此时len(s)>len(t)则表示不合法。
                if len(s) > len(t):
                    return ""
        # 经过上述处理，得到每个字母和对应的比其小的字母
        VISITING, VISITED = 1, 2  # 标记符号：访问中、已访问
        states = {}
        order = []

        def dfs(u: str) -> bool:
            states[u] = VISITING  # 来到当前节点，标记为访问中。
            for v in g[u]:  # 遍历比u大的字母
                if v not in states:  # 如果没有访问过，则访问该节点
                    if not dfs(v):
                        return False
                elif states[v] == VISITING:  # 正在访问中，则表示形成了环，直接返回false
                    return False
            order.append(u)  # 先访问所有比u大的字母，最后再放入u。
            states[u] = VISITED  # 结束时，标记为已访问。
            return True

        return ''.join(reversed(order)) if all(dfs(u) for u in g if u not in states) else ""

# 作者：LeetCode-Solution
# 链接：https://leetcode.cn/problems/Jf1JuT/solution/wai-xing-wen-zi-dian-by-leetcode-solutio-to66/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
