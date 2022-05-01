class TrieNode:
    def __init__(self):
        self.path = 0
        self.end = 0
        self.nexts = [None]*26


class TrieTree:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        if word is None:
            print("--")
            return
        head = self.root
        head.path += 1
        for i in word:
            index = ord(i) - ord('a')
            if head.nexts[index] is None:
                head.nexts[index] = TrieNode()
            head = head.nexts[index]
            head.path += 1
        head.end += 1

    # 删除一次
    def delete(self, word):
        if self.search(word) != 0:
            head = self.root
            head.path -= 1
            for i in word:
                index = ord(i) - ord("a")
                head.nexts[index].path -= 1
                if head.nexts[index].path == 0:
                    head.nexts[index] = None
                    return
                head = head.nexts[index]
            head.end -= 1

    # 返回word加入的次数
    def search(self, word):
        if word is None:
            return 0
        head = self.root
        for i in word:
            index = ord(i) - ord('a')
            if head.nexts[index] is None:
                return 0
            head = head.nexts[index]
        return head.end

    # 以word为前缀的单词出现过几次
    def prefixNumber(self,word):
        if word is None:
            return 0
        head = self.root
        for i in word:
            index = ord(i) - ord('a')
            if head.nexts[index] is None:
                return 0
            head = head.nexts[index]
        return head.path



if __name__ == "__main__":
    tree1 = TrieTree()
    tree1.insert("abc")
    tree1.insert("abc")
    tree1.insert("cds")
    tree1.insert("acb")
    print(tree1.search("abc"))
    print(f"以ab为前缀的单词出现了{tree1.prefixNumber('ab')}次")
    tree1.delete("abc")
    print(tree1.search("abc"))
    print(f"以ab为前缀的单词出现了{tree1.prefixNumber('ab')}次")
    # print(tree1.root.path)
    # print(tree1.root.nexts[0].path)
    # print(tree1.root.nexts[0].nexts[1].path)
    # print(tree1.root.nexts[0].nexts[1].nexts[2].path)
    # print(tree1.root.nexts[0].nexts[1].nexts[2].end)
    # print(tree1.root.nexts[0].nexts[1].nexts[3].path)
