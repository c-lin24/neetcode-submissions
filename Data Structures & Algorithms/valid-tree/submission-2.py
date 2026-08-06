class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False

        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visited = [False] * n

        def dfs(node: int, parent: int):
            visited[node] = True
            for v in adj[node]:
                if v == parent: 
                    continue
                if visited[v]:
                    return True
                if dfs(v, node):
                    return True
            return False


        return not dfs(0,-1)
        