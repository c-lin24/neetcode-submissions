class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        for point in points:
            dis = math.sqrt((point[0])**2 + (point[1])**2)
            if len(heap) < k:
                heapq.heappush(heap, (-dis, point))
            elif -dis > heap[0][0]:
                heapq.heappop(heap)
                heapq.heappush(heap, (-dis, point))
                
        return [h[1] for h in heap]