class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_dict = {}
        s2_dict = {}
        n = len(s1)
        l = 0
        if n > len(s2):
            return False

        for ch in s1:
            s1_dict[ch] = s1_dict.get(ch, 0) + 1
        
        for i in range(n):
            s2_dict[s2[i]] = s2_dict.get(s2[i], 0) + 1
        
        if s2_dict == s1_dict:
            return True

        for r in range(n, len(s2)):
            s2_dict[s2[r]] = s2_dict.get(s2[r], 0) + 1

            if s2_dict[s2[l]] == 1:
                del s2_dict[s2[l]]
            else: 
                s2_dict[s2[l]] -= 1  
            if s2_dict == s1_dict: 
                return True
            l += 1

        return False
