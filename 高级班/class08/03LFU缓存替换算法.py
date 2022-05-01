# KMP算法扩展题目二
# 一个缓存结构需要实现如下功能
# void set(int key, int value)：加入或修改key对应的value
# int get(int key)：查询key对应的value值
# 但是缓存中最多放K条记录，如果新的第K+1条记录要加入，就需要根据策略删掉一条记录，
# 然后才能把新记录加入。
# 这个策略为：在缓存结构的K条记录中，哪一个key从进入缓存结构的时刻开始，被调用
# set或者get的次数最少，就删掉这个key的记录；如果调用次数最少的key有多个，上次调
# 用发生最早的key被删除。
# 这就是LFU缓存替换算法。实现这个结构，K作为参数给出。O(1)

# 词频由不同桶来记录，上次调用的时间由每个桶内的双向链表的先后顺序记录
class Node:  # 链表的节点属性,val保存key和value,是一个二维的
    def __init__(self, value, next=None, pre=None):
        self.val = value
        self.wofru = 1
        self.next = next
        self.pre = pre


class tong:  # 桶内要放一个双向链表，所以val放表头和表尾节点
    def __init__(self, value, next=None, pre=None):
        self.val = value
        self.next = next
        self.pre = pre
        self.size = 2


class LFUcache:
    def __init__(self, k):
        self.hashmap = {}  # 利用哈希表记录每个key对应的节点
        self.hashfrutong = {}  # 利用哈希表记录每个词频对应的桶
        self.headtong = tong(None)  # 新建两个表示头和尾的空桶
        self.tailtong = tong(None)
        self.headtong.next = self.tailtong
        self.tailtong.pre = self.headtong
        self.k = k  # 表示能容纳的记录个数

    def set(self, key, value):
        if key in self.hashmap:  # 当前节点已经有记录了
            curnode = self.hashmap[key]
            curnode.val[1] = value  # 修改对应的value
            curtong = self.hashfrutong[curnode.wofru]
            curnode.pre.next = curnode.next  # 从原来链表中删除改节点
            curnode.next.pre = curnode.pre
            curnode.wofru += 1
            self.changetong(curnode, curtong)
            curtong.size -= 1  # 原来桶的尺寸-1
            self.isdeltong(curnode, curtong)  # 判断-1后是否为空
        else:  # 没有该key
            if self.k == 0:  # 处理容量为0的特殊情况
                return -1
            if len(self.hashmap) == self.k:  # 当前已经满了
                curtong = self.headtong.next  # 头桶的后面的一个桶
                delnode = curtong.val[0].next  # 要删除的节点
                del self.hashmap[delnode.val[0]]  # 将该节点对应的记录从哈希表中删除
                delnode.pre.next = delnode.next  # 将该节点从双向链表中删除
                delnode.next.pre = delnode.pre
                curtong.size -= 1
                if curtong.size == 2:  # 如果当前桶包含要删除的节点只有二个节点，则删除该桶
                    curtong.pre.next = curtong.next
                    curtong.next.pre = curtong.pre
                    del self.hashfrutong[delnode.wofru]
            curnode = Node([key, value])
            self.hashmap[key] = curnode  # 添加该key对应的节点
            curtong = self.headtong  # 将新桶放到头桶的后面
            self.changetong(curnode, curtong)

    def get(self, key):
        if key in self.hashmap:
            curnode = self.hashmap[key]
            curtong = self.hashfrutong[curnode.wofru]
            curnode.pre.next = curnode.next  # 从原来链表中删除改节点
            curnode.next.pre = curnode.pre
            curnode.wofru += 1
            self.changetong(curnode, curtong)
            curtong.size -= 1
            self.isdeltong(curnode, curtong)
            return curnode.val[1]
        else:
            return -1

    def changetong(self, curnode, curtong):
        if curnode.wofru in self.hashfrutong:  # 有目标词频的桶
            targettong = self.hashfrutong[curnode.wofru]
            targettong.size += 1  # 桶的容量加一
            targettongtail = targettong.val[1]  # 获取到目标桶的尾节点
            targettongtail.pre.next = curnode  # 尾节点的上一个节点处插入
            curnode.pre = targettongtail.pre
            curnode.next = targettongtail
            targettongtail.pre = curnode
        else:  # 没有目标词频的桶
            newnodehead, newnodetail = Node(None), Node(None)  # 新创建的双向链表
            newnodehead.next = curnode
            curnode.pre = newnodehead
            curnode.next = newnodetail
            newnodetail.pre = curnode
            targettong = tong([newnodehead, newnodetail])  # 新建桶
            targettong.size += 1  # 新桶尺寸包含新加入节点为3
            self.hashfrutong[curnode.wofru] = targettong  # 更新词频桶
            targettong.pre = curtong  # 将新桶插入其中
            targettong.next = curtong.next
            curtong.next.pre = targettong
            curtong.next = targettong

    def isdeltong(self, curnode, curtong):
        if curtong.size == 2:  # 如果当前桶包含要删除的节点只有二个节点，则删除该桶
            curtong.pre.next = curtong.next
            curtong.next.pre = curtong.pre
            del self.hashfrutong[curnode.wofru - 1]  # 删除该词频增加之前的桶


lfu = LFUcache(3)
# lfu.set('a', 1)
# lfu.set('b', 2)
# lfu.set('c', 3)
# lfu.get('a')
# lfu.set('d', 4)
# lfu.set('c', 5)
# print(lfu.get('a'))
# print(lfu.get('b'))
# print(lfu.get('c'))
lfu.set(0, 0)
print(lfu.get(0))
