class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # number of edges = number of nodes because we have 1 cycle
        n = len(edges)  
        parents = [i for i in range (n + 1)] #ith node -> parent (1 - n)
        rank = [1] * (n + 1)

        def find(n):
            if n != parents[n]:
                parents[n] = find(parents[n])
            return parents[n]
            
        def union(n1, n2):

            p1, p2 = find(n1), find(n2)  #find both parents

            if p1 == p2:
                return False

            if rank[p1] > rank[p2]:
                parents[p2] = p1
                rank[p1] += rank[p1]
            else: 
                parents[p1] = p2   
                rank[p2] += rank[p1]

            return True

        
        for n1, n2 in edges:
            if not union(n1, n2):
                return [n1, n2]
