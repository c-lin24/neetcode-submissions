class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        return self.createDic(s) == self.createDic(t)

    def createDic(self, string: str) -> dict: 
        d = {}
        for s in string: 
            if s in d: 
                d[s] += 1
            else: 
                d[s] = 1

        return d
        
        