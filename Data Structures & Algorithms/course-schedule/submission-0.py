class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        adj_list = defaultdict(list)
        for pair in prerequisites:
            adj_list[pair[1]].append(pair[0])

        visited = set()
        in_path = set()

        def has_cycle(node: int) -> bool: 
            if node in in_path: 
                return True
            if node in visited: 
                return False 

            in_path.add(node)
            
            for i in adj_list[node]:
                if has_cycle(i):
                    return True
        
            in_path.remove(node)
            visited.add(node)
            return False

        for course in range(numCourses):
            if has_cycle(course):
                return False

        return True 
            