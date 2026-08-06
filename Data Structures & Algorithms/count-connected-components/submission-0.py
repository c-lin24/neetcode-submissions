class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)


        visited = [False] * n

        def dfs(node: int): 
            visited[node] = True
            for num in adj[node]:
                if not visited[num]:
                    dfs(num)
        
        comps = 0 

        for i in range(n):
            if not visited[i]:
                comps += 1
                dfs(i)

        return comps


    