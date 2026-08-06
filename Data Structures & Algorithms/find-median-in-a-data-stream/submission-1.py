class MedianFinder:

    def __init__(self):
        self.small = []  # max heap --> lower half [3,3,2,1]
        self.big = []    # min heap --> upper half [3,4]

    def addNum(self, num: int) -> None:
        if self.big and num >= self.big[0]: 
            heapq.heappush(self.big, num)
        else: 
            heapq.heappush(self.small, -num)

        if len(self.small) + 1 < len(self.big): 
            transfer = heapq.heappop(self.big) 
            heapq.heappush(self.small, -transfer)

        elif len(self.big) + 1 < len(self.small):
            transfer = -heapq.heappop(self.small)
            heapq.heappush(self.big, transfer)

    def findMedian(self) -> float:
        if (len(self.small) + len(self.big)) % 2 == 0:
            return (-1 * self.small[0] + self.big[0]) / 2
        
        if len(self.small) > len(self.big): 
            return -1 * self.small[0]
        else:
            return self.big[0]