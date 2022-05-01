import heapq


class MedianHolder():
    def __init__(self):
        self.maxqueue = []
        self.minqueue = []

    def modifyTwoHeapsSize(self):
        if len(self.maxqueue) == len(self.minqueue) + 2:
            heapq.heappush(self.minqueue, -heapq.heappop(self.maxqueue))
        if len(self.minqueue) == len(self.maxqueue) + 2:
            heapq.heappush(self.maxqueue, -heapq.heappop(self.minqueue))

    def addNumber(self, num):
        if (len(self.maxqueue) == 0) or (num <= (-self.maxqueue[0])):
            heapq.heappush(self.maxqueue, -num)
        else:
            heapq.heappush(self.minqueue, num)
        self.modifyTwoHeapsSize()

    def getMedian(self):
        if len(self.minqueue) + len(self.maxqueue) == 0:
            return None
        if len(self.minqueue) > len(self.maxqueue):  # 偶数
            return self.minqueue[0]
        elif len(self.maxnqueue) > len(self.minqueue):
            return -self.maxqueue[0]
        else:
            return (self.minqueue[0] - self.maxqueue[0]) / 2


if __name__ == "__main__":
    median = MedianHolder()
    median.addNumber(1)
    # median.addNumber(2)
    print(median.getMedian())
    # median.addNumber(3)
    # print(median.getMedian())
