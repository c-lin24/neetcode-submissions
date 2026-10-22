class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        adj = [[] for _ in range(n)]
        for s, d, w in edges:
            adj[s].append((d, w))

        dist = [float('inf')] * n
        dist[src] = 0
        heap = [(0, src)]

        while heap:
            d, u = heapq.heappop(heap)
            if d > dist[u]:          # stale entry, a better path was already found
                continue

            # one entry gets through for each node
            for v, w in adj[u]:
                if d + w < dist[v]:  # found a shorter route to v
                    dist[v] = d + w
                    heapq.heappush(heap, (dist[v], v))

        return {i: (dist[i] if dist[i] != float('inf') else -1) for i in range(n)}